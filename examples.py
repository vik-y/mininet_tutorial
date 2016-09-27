#!/usr/bin/python
# Example taken from mininet official github repo
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.node import RemoteController
from mininet.log import setLogLevel, debug


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

'''
In mininet you must understand a few important things:
Mininet is made of up of a topology which is made up of nodes. That's why in the simplesTest() function above:

topo = SingleSwitchTopo(n=10) # We first create a topology
net = Mininet(topo) # Then we create a mininet with that topology
c1 = RemoteController(name='c1', ip='192.168.56.1') #  we create a new controller
net.addController(c1) # And add the newly created controller to the existing mininet.

And then we start all our simulation
We must note that "Node", "Net", "Topo" are three major components of mininet.
'''
def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=10)
    net = Mininet(topo)
    c1 = RemoteController(name='c1', ip='192.168.56.1')
    net.addController(c1)
    #net.build()
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    # Running programs in a host
    h1 = net.get('h1')
    result = h1.cmd('ifconfig')
    print result
    net.stop()


if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()