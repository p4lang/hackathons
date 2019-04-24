import random

from p4app import P4Mininet
from mininet.topo import SingleSwitchTopo

topo = SingleSwitchTopo(2)
net = P4Mininet(program='registers.p4', topo=topo)
net.start()

h1 = net.get('h1')
h2 = net.get('h2')

out = h1.cmd('./send.py 10.0.0.2 write fooo')
print('sent a write packet with payload *fooo* and received: %s' % out)
assert out.strip() == "fooo"

out = h1.cmd('./send.py 10.0.0.2 read barr')
print('sent a read packet with payload *barr* and received: %s' % out)
assert out.strip() == "fooo"

out = h1.cmd('./send.py 10.0.0.2 read bazz')
print('sent a write packet with payload *bazz* and received: %s' % out)
assert out.strip() == "fooo"

out = h1.cmd('./send.py 10.0.0.2 write foo1')
print('sent a write packet with payload *foo1* and received: %s' % out)
assert out.strip() == "foo1"

out = h1.cmd('./send.py 10.0.0.2 read bar1')
print('sent a read packet with payload *barr* and received: %s' % out)
assert out.strip() == "foo1"

# uncomment these two lines to stop on Mininet CLI for further debugging
#from mininet.cli import CLI
#CLI(net)

print "Quit."
