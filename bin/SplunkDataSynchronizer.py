import SplunkConnector

class SplunkDataSynchronizer(object):
        
        splunkConnection = None
        
        def __init__(self, splunkConnector):
                self.splunkConnection = splunkConnector

        def getLatestDataRow(self):
                self.splunkConnection = self.splunkConnection.blockingSearch("head")
