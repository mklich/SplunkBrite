import splunklib
import splunklib.client as client

class SplunkConnector(object):
        def __init__(self,host,port,username,password):
                self.splunkClient = client.connect(host=host,port=port,username=username,password=password)

        def blockingSearch(self,query):
                kwargs = {"exec_mode": "blocking"}
                job = self.splunkClient.jobs.create(query,**kwargs)
                return job


#search = SplunkConnector("localhost","8089","admin","changeme")
#job = search.blockingSearch("head 1")
#print job
