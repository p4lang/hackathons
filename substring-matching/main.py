# Copyright 2019 Contributors of the p4 hackathon (https://github.com/pl-ca/p4hackathon)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from p4app import P4Mininet, P4Program
from mininet.topo import Topo
from mininet.cli import CLI
from p4app import P4Mininet
from mininet.topo import SingleSwitchTopo

if len(sys.argv) > 1:
    if sys.argv[1] == 'compile':
        try:
            P4Program('substring_match.p4').compile()
        except Exception as e:
            print(e)
            sys.exit(1)
        sys.exit(0)


topo = SingleSwitchTopo(1)
net = P4Mininet(program='substring_match.p4', topo=topo)
net.start()



sw = net.get('s1')

for i in range(0,8):
    sw.insertTableEntry(table_name='MyIngress.get_strA_char',
                        match_fields={'hdr.internal_header.iterator_r': i},
                        action_name='MyIngress.get_strA_char'+str(i)
                        )

for i in range(0,8):
    sw.insertTableEntry(table_name='MyIngress.get_strB_char',
                        match_fields={'hdr.internal_header.iterator_l': i},
                        action_name='MyIngress.get_strB_char'+str(i)
                        )


for x in range (0, 8):
    sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                        priority = 1,
                        match_fields={ 'hdr.internal_header.iterator_l': [0x00000000, 0xFFFFFFFF],
                                       'hdr.internal_header.iterator_r': [x+1, 0xFFFFFFFF]},
                        action_name='MyIngress.IncrementCount.set_l0_count',
                        action_params={'val': 1 << (x*8)}
                        )

sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [1, 0xFFFFFFFF],
                                   'hdr.internal_header.iterator_r': [0, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.set_l1_first'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [2, 0xFFFFFFFF],
                                   'hdr.internal_header.iterator_r': [0, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.set_l2_first'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [3, 0xFFFFFFFF],
                                   'hdr.internal_header.iterator_r': [0, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.set_l3_first'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [4, 0xFFFFFFFF],
                                   'hdr.internal_header.iterator_r': [0, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.set_l4_first'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [5, 0xFFFFFFFF],
                                   'hdr.internal_header.iterator_r': [0, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.set_l5_first'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [6, 0xFFFFFFFF],
                                   'hdr.internal_header.iterator_r': [0, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.set_l6_first'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [7, 0xFFFFFFFF],
                                   'hdr.internal_header.iterator_r': [0, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.set_l7_first'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [1, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.increment_l1_count'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [2, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.increment_l2_count'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [3, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.increment_l3_count'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [4, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.increment_l4_count'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [5, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.increment_l5_count'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [6, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.increment_l6_count'
                    )
sw.insertTableEntry(table_name='MyIngress.IncrementCount.increment_count',
                    priority = 1,
                    match_fields={ 'hdr.internal_header.iterator_l': [7, 0xFFFFFFFF]},
                    action_name='MyIngress.IncrementCount.increment_l7_count'
                    )



from mininet.cli import CLI
CLI(net)

print "OK"
