import networkx as nx
import json
import urllib.request
import numpy as np
import pylab


def get_all_switches():
    url = "http://0.0.0.0:8080/v1.0/topology/switches"
    resp = urllib.request.urlopen(url)
    res = resp.read()
    res = str(res, 'utf-8')

    res = json.loads(res)  # list
    flag = 1
    for re in res:  # 不同的交换机  re:字典
        print()
        print("交换机 ------", flag, "------------")
        print("交换机IP ----", re['dpid'])
        print("交换机端口 --")
        for port in re['ports']:
            print("端口--", port)
        flag = flag + 1


def get_switches():
    url = "http://0.0.0.0:8080/stats/switches"
    resp = urllib.request.urlopen(url)
    res = resp.read()
    res = str(res, 'utf-8')
    res = json.loads(res)  # list
    return res


# [1, 2, 3, 4, 5, 6]


def get_all_links():
    url = "http://0.0.0.0:8080/v1.0/topology/links"
    resp = urllib.request.urlopen(url)
    res = resp.read()
    res = str(res, 'utf-8')
    res = json.loads(res)  # list
    flag = 1
    # for re in res:  # 不同的交换机  re:字典
    #     print()
    #     print("链路 ------", flag, "------------")
    #     print("源点端口")
    #     print("所属交换机", re["src"]["dpid"])
    #     print("端口MAC   ", re["src"]["hw_addr"])
    #     print("端口名称  ", re["src"]["name"])
    #     print("端口号    ", re["src"]["port_no"])
    #     print("终点端口")
    #     print("所属交换机", re["dst"]["dpid"])
    #     print("端口MAC   ", re["dst"]["hw_addr"])
    #     print("端口名称  ", re["dst"]["name"])
    #     print("端口号    ", re["dst"]["port_no"])
    #     flag = flag + 1

    return res


def get_flow_table():
    dpid = "2"
    url = "http://0.0.0.0:8080/stats/flow/" + dpid
    resp = urllib.request.urlopen(url)
    res = resp.read()
    res = str(res, 'utf-8')
    res = json.loads(res)  # list
    print(res)


DpIdList = get_switches()
G = nx.Graph()

for id in DpIdList:
    G.add_node(int(id))

DpLinks = get_all_links()
flag = 1
for re in DpLinks:  # 不同的交换机  re:字典
    print()
    print("链路 ------", flag, "------------")
    G.add_edge((int(re["src"]["dpid"])), (int(re["dst"]["dpid"])))
    # print("源点端口")
    # print("所属交换机", int(re["src"]["dpid"]))
    # print("端口MAC   ", re["src"]["hw_addr"])
    # print("端口名称  ", re["src"]["name"])
    # print("端口号    ", re["src"]["port_no"])
    #
    # print("终点端口")
    # print("所属交换机", re["dst"]["dpid"])
    # print("端口MAC   ", re["dst"]["hw_addr"])
    # print("端口名称  ", re["dst"]["name"])
    # print("端口号    ", re["dst"]["port_no"])
    flag = flag + 1
print(G.edges())

pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=True)
# pylab.show()

p = nx.shortest_path(G, source=1, target=6)
print("最短路径", p)
print("最短路径值 ", len(p))
