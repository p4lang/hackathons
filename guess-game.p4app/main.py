# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

from p4app import P4Mininet
from mininet.topo import SingleSwitchTopo

topo = SingleSwitchTopo(2)
net = P4Mininet(program='registers.p4', topo=topo)
net.start()

h1 = net.get('h1')
h2 = net.get('h2')

n = random.randint(1, 9)

str_to_send = './send.py 10.0.0.2 write %d' % n
out = h1.cmd(str_to_send)
print('wrote secret number %d to switch dataplane' % n)
print('Pretend that you do not know the secret number and try to guess it. Start now.')
assert int(out) == n

guess = int(raw_input("Enter an integer from 1 to 9: "))

while n != "guess":
    str_to_send = './send.py 10.0.0.2 read %d' % guess
    print('str_to_send = %s' % str_to_send)
    out = h1.cmd(str_to_send)
    # print('out = %s' % out)
    outcome = int(out.strip())
    # print('outcome = %s' % outcome)
    if outcome == 0:
        print('Congrats!')
        break
    elif outcome == 1:
        print('Hidden number is smaller')
    else:
        print('Hidden number is larger')
    
    guess = int(raw_input("Enter an integer from 1 to 9: "))

print('Game over, bye.')

# comment out to end the program in Mininet terminal
#from mininet.cli import CLI
#CLI(net)

print "Quit."
