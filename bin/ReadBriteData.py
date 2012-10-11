import urllib2
from xml.dom.minidom import parseString
from datetime import datetime

uri = "https://www.eventbrite.com/xml/event_search?app_key=2ZFPC3WOTA4UPERJKG&country=US&max=10"

def GetSearchData(uri):
	searchResultsXml = urllib2.urlopen(uri)
	xmlData = searchResultsXml.read()
	searchResultsXml.close()
	dom = parseString(xmlData)
	output = ''
	for x in dom.getElementsByTagName('event'):

		#timestamp =  str(datetime.now()) 
		id = "id=\"" + x.getElementsByTagName('id')[0].firstChild.nodeValue + "\""
		title = "title=\"" + x.getElementsByTagName('title')[0].firstChild.nodeValue +"\""
		timestamp = "created=" + x.getElementsByTagName('created')[0].firstChild.nodeValue
		long = "latitude=\"" + x.getElementsByTagName('latitude')[0].firstChild.nodeValue + "\""
		lat = "longitude=\"" + x.getElementsByTagName('longitude')[0].firstChild.nodeValue + "\""
		output =  timestamp+' '+id+' '+title+' '+long+' '+lat
		print output	

GetSearchData(uri)


