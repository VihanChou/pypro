import urllib2
import json

def add_flow_entry(dpid,match,priority,actions):
    url = "http://127.0.0.1:8080/stats/flowentry/add"
    post_data = "{'dpid':%s,'match':%s,'priority':%s,'actions':%s}" % (dpid,str(match),priority,str(actions))
    req = urllib2.Request(url,post_data)
    res = urllib2.urlopen(req)
    return res.getcode()


match = {'dl_src':'36:4c:24:24:3b:4d','in_port':'2','dl_dst': '46:c8:c0:4c:ef:40'}
actions = [{"type":"OUTPUT","port":1}]
print(add_flow_entry('1',match,'3433',actions))


match = {'dl_src':'46:c8:c0:4c:ef:40','in_port':'1','dl_dst': '36:4c:24:24:3b:4d'}
actions = [{"type":"OUTPUT","port":2}]
print(add_flow_entry('1',match,'3434',actions))


