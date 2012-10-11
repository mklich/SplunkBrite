import urllib2
from xml.dom.minidom import parseString
from datetime import datetime
from SplunkDataSynchronizer import SplunkDataSynchronizer
from SplunkConnector import SplunkConnector

splunk = SplunkConnector("localhost",8089,"admin","changeme")

synchronizer = SplunkDataSynchronizer(splunk)
lastId = synchronizer.getLastInputId()

maxValues = 50

uri = "https://www.eventbrite.com/xml/event_search?app_key=2ZFPC3WOTA4UPERJKG&country=US&max="+str(maxValues)

if lastId != None:
        uri = uri +"&since_id="+str(lastId)
else:
        uri = uri +"&date_created=Today"

def GetSearchData(uri):
	searchResultsXml = urllib2.urlopen(uri)
	xmlData = searchResultsXml.read()
	searchResultsXml.close()
	dom = parseString(xmlData)
	output = ''
	for x in dom.getElementsByTagName('event'):
		timestamp =  x.getElementsByTagName('created')[0].firstChild.nodeValue
		id = "id=\"" + x.getElementsByTagName('id')[0].firstChild.nodeValue + "\""
		title = "title=\"" + x.getElementsByTagName('title')[0].firstChild.nodeValue +"\""
		created = "created=" + x.getElementsByTagName('created')[0].firstChild.nodeValue
		long = "latitude=\"" + x.getElementsByTagName('latitude')[0].firstChild.nodeValue + "\""
		lat = "longitude=\"" + x.getElementsByTagName('longitude')[0].firstChild.nodeValue + "\""
		output = timestamp+' '+id+ ' '+created+' '+title+' '+long+' '+lat
		print output	

GetSearchData(uri)


