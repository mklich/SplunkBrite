from xml.dom.minidom import parseString

#
# Constants
#
PARENT_TAG_NAME = "event"

# List containing the name of the tag aswell as the name that will be parsed as a field in Splunk 
LIST_OF_FIELDS = [("id","id"), \
                ("title","title"), \
                ("created","created"), \
                ("latitude","latitude"), \
                ("longitude","longitude"), \
                ("organizer","organizer.name")]


TIMESTAMP_FIELD = "created"                    

class EventBriteDataParser:
        
        def __init__(self, xmlData):
                self.xmlData = xmlData

        def __getXmlData(self, parentDOM, tagName):
                
                # If there is a dot in the tagName, it means that we have a nested field
                # so we recursively crawl down the xml tree
                if "." in tagName:
                        parentTag = tagName.split('.')[0]
                        childTag = tagName[tagName.find('.')+1:]
                        newParentDom = parentDOM.getElementsByTagName(parentTag)[0]
                        return self.__getXmlData(newParentDom,childTag)
               
                # If a field does not exist, Skip..
                if parentDOM == None or parentDOM.getElementsByTagName(tagName)[0] == None or parentDOM.getElementsByTagName(tagName)[0].length == 0 or  parentDOM.getElementsByTagName(tagName)[0].firstChild == None: 
                        return None

                return parentDOM.getElementsByTagName(tagName)[0].firstChild.nodeValue
        
        def __getFieldAndValueRow(self,field,value):
                if value == None:
                        return ""
                return "=".join([field,value.join(["\"","\""])])

        def __getEventBriteDataRow(self, parentDOM):
                result = ""
                # Add timestamp
                result = self.__getXmlData(parentDOM, TIMESTAMP_FIELD) + " "
                
                result += " ".join([self.__getFieldAndValueRow(field[0],self.__getXmlData(parentDOM,field[1])) for field in LIST_OF_FIELDS])
                
                return result

        def __parseXmlData(self, xmlData):
                dom = parseString(xmlData)

                parsedData = "\n".join([self.__getEventBriteDataRow(eventDOM) for eventDOM in dom.getElementsByTagName(PARENT_TAG_NAME)])

                return parsedData

        def getSplunkInput(self):
                if self.xmlData == None:
                        return ""
                else:
                        return self.__parseXmlData(self.xmlData)
