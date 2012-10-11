import urllib2
from xml.dom.minidom import parseString

uri = "https://www.eventbrite.com/xml/event_search?app_key=2ZFPC3WOTA4UPERJKG&city=San+Francisco&date=This+month"

def GetSearchData(uri):
	searchResultsXml = urllib2.urlopen(uri)
	xmlData = searchResultsXml.read()
	searchResultsXml.close()
	dom = parseString(xmlData)
	
	for x in dom.getElementsByTagName('event'):
		#xmlTag = x.toxml()
		print x.getElementsByTagName('id')[0].firstChild.nodeValue
		print x.getElementsByTagName('title')[0].firstChild.nodeValue
		print x.getElementsByTagName('created')[0].firstChild.nodeValue
		print x.getElementsByTagName('latitude')[0].firstChild.nodeValue
		print x.getElementsByTagName('longitude')[0].firstChild.nodeValue
			

GetSearchData(uri)


