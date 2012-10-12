import urllib2
from xml.dom.minidom import parseString
from datetime import datetime
from SplunkDataSynchronizer import SplunkDataSynchronizer
from SplunkConnector import SplunkConnector
from EventBriteDataParser import EventBriteDataParser

lastId = None
#splunk = SplunkConnector("localhost",8089,"admin","changeme")

#synchronizer = SplunkDataSynchronizer(splunk)
#lastId = synchronizer.getLastInputId()

maxValues = 25

uri = "https://www.eventbrite.com/xml/event_search?app_key=2ZFPC3WOTA4UPERJKG&country=US&max="+str(maxValues)

if lastId != None:
        uri = uri +"&since_id="+str(lastId)
else:
        uri = uri +"&date_created=Today"

def GetSearchData(uri):
	searchResultsXml = urllib2.urlopen(uri)
	xmlData = searchResultsXml.read()
        searchResultsXml.close()
        
        eventData = EventBriteDataParser(xmlData)
        
        print eventData.getSplunkInput()


GetSearchData(uri)


