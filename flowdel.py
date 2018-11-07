import urllib2
import json

def delete_flow_entry(dpid, match=None, priority=None, actions=None):
    url = "http://127.0.0.1:8080/stats/flowentry/delete"
    post_data = "{'dpid':%s" % dpid
    if match is not None:
        post_data += ",'match':%s" % str(match)
    if priority is not None:
        post_data += ",'priority':%s" % priority
    if actions is not None:
        post_data += ",'actions':%s" % str(actions)
    post_data += "}"

    req = urllib2.Request(url,post_data)
    res = urllib2.urlopen(req)
    return res.getcode()


print(delete_flow_entry(1))

#http://127.0.0.1:8080/stats/flowentry/delete
