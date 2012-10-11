import SplunkConnector
import SplunkBriteConstants as Constants

class SplunkDataSynchronizer(object):
        
        def __init__(self, splunkConnector):
                self.splunkConnection = splunkConnector

        def getLatestEventTimestampFromSplunkData(self):
                dataRow = self.__getLatestDataRow()
                return __getTimestampFromDataRow(dataRow)

        def __getTimestampFromDataRow(self,dataRow):
                return dataRow[0][Contants.SPLUNK_TIMESTAMP_FIELD_NAME]

        def __getLatestDataRow(self):
                searchForLatestDataRow = "index = \""+ Constants.SPLUNK_INDEX_NAME +"\" | " \
                                "sourcetype=\""+ Constants.SPLUNK_SOURCETYPE_FIELD_NAME +"\"" \
                                " | sort - "+SPLUNK_TIMESTAMP_FIELD_NAME 
                self.splunkConnection = self.splunkConnection.blockingSearch(searchForLatestDataRow)

