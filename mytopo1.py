from mininet.topo import Topo
class MyProxyTopo( Topo ):       #继承于TOPO类

    def __init__( self ):   #构造方法中初始化节点,链接

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1      = self.addHost( 'h1' )
        h2      = self.addHost( 'h2' )
       
        s1      = self.addSwitch( 's1' )
        s2      = self.addSwitch( 's2' )
        s3      = self.addSwitch( 's3' )
        s4      = self.addSwitch( 's4' )
        s5      = self.addSwitch( 's5' )
        s6      = self.addSwitch( 's6' )


        # Add links
        self.addLink( s1,s2)
        self.addLink( s1,s5)
        
        self.addLink( s2,s3)
        self.addLink( s2,s4)
        
        self.addLink( s3,s6)

        self.addLink( s4,s5)
        
        self.addLink( s5,s6)


        self.addLink( h1,s1)
        self.addLink( h2,s3)


topos = { 'MyProxyTopo': ( lambda: MyProxyTopo() ) }   #使用自己定义的类来进行变量初始化