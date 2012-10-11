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

		timestamp =  str(datetime.now()) 
		a = "id=\"" + x.getElementsByTagName('id')[0].firstChild.nodeValue + "\""
		b = "title=\"" + x.getElementsByTagName('title')[0].firstChild.nodeValue +"\""
		c = "created=[" + x.getElementsByTagName('created')[0].firstChild.nodeValue + "]"
		d = "latitude=\"" + x.getElementsByTagName('latitude')[0].firstChild.nodeValue + "\""
		e = "longitude=\"" + x.getElementsByTagName('longitude')[0].firstChild.nodeValue + "\""
		output =  timestamp+' '+a+' '+b+' '+c+' '+d+' '+e
		print output	

GetSearchData(uri)


