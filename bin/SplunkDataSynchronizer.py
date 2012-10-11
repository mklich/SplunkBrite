# -*- coding: utf-8 -*-

from SplunkConnector import SplunkConnector

import SplunkBriteConstants as Constants
import splunklib.results as results

class SplunkDataSynchronizer(object):
        
        def __init__(self, splunkConnector):
                self.splunkConnection = splunkConnector

        def getLatestEventTimestampFromSplunkData(self):
                dataRow = self.__getLatestDataRowBasedOnId()
                return self.__getTimestampFromDataRow(dataRow)

        def getLastInputId(self):
                dataRow = self.__getLatestDataRowBasedOnId()
                #for result in results.ResultsReader(dataRow.results()):
                #        print result
                
                return self.__getIdFromDataRow(dataRow)
        
        def __getIdFromDataRow(self,dataRow):
                result = None
                for result in results.ResultsReader(dataRow.results()):
                        pass

                if result == None:
                        return None
                else:
                        return result[1]["id"]

        def __getLatestDataRowBasedOnId(self):
                searchForLatestDataRow="search index=\""+Constants.SPLUNK_INDEX_NAME +"\" sourcetype=\""+Constants.SPLUNK_SOURCETYPE_FIELD_NAME+"\" | sort - "+Constants.SPLUNK_ID_FIELD_NAME+" | head 1 | table "+Constants.SPLUNK_ID_FIELD_NAME+""
                return self.splunkConnection.blockingSearch(searchForLatestDataRow)

