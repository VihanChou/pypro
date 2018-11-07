from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import HANDSHAKE_DISPATCHER
from ryu.controller.handler import CONFIG_DISPATCHER
from ryu.controller.handler import DEAD_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0#在这里导入使用的控制器版本支持包

import time;

class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]#在这里定义控制器版本

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)
        
        # 这个装饰器告诉函数在什么时候被调用
        # (装饰器的第一个参数标识了在什么事件下该函数会被调用,装饰器的第二个参数标识了在交换机的何种状态下)
        # 使用MAIN_DISPATCHER表示只有控制器和交换机交流完成后才进行通信
        #
    
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):   #根据装饰器,这个函数在有Packet_In消息的时候就会被调用
        print("sir i got a packet_in")
        msg = ev.msg       #代表了一个packet_in数据包对象
        dp = msg.datapath  # represents a datapath (switch).
        ofp = dp.ofproto   #dp.ofproto,dp.ofproto_parser表示Ryu和交换机进行通信的Openflow协议
        ofp_parser = dp.ofproto_parser

        actions = [ofp_parser.OFPPacketOut(ofp.OFPP_FLOOD)]  #OFPActionOutput 使用packet_out消息来指定你想要发送的数据到哪一个交换机端口vOFPP_FLOOD 标志着这个数据包应该发送到所有端口
        out = ofp_parser.OFPPacketOut(
            datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port,
            actions=actions)          #OFPPacketOut类用于创建packet_out消息
        dp.send_msg(out)   #使用Openflow消息对象调用datapath类的send_message方法, Ryu就会构建并发送一个on-wire数据格式到这个交换机)

    @set_ev_cls(ofp_event.EventOFPEchoRequest, MAIN_DISPATCHER)  #用于捕获ECHO_REQUEST 消息的函数
    def echo_request_handler(self, ev):
        print("sir i got a ECHO_REQUEST")
  
   
    @set_ev_cls(ofp_event.EventOFPHello, HANDSHAKE_DISPATCHER)
    def get_Hello(self , ev):
        print("sir i got a Hello")
 
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures , MAIN_DISPATCHER)
    def switch_features_handler(self , ev):
        print("sir i got a  SwitchFeatures")
    
#OFPT_ECHO_REQUEST
#OFPT_ECHO_REPLY




