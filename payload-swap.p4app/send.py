#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import socket
import struct

UDP_PORT = 1234
OP_READ   = 0
OP_WRITE   = 1

hdr = struct.Struct('!B 4s') # op_type [val]

if len(sys.argv) < 4:
    print "Usage: %s HOST READ|WRITE [VALUE]" % sys.argv[0]
    sys.exit(1)

host = sys.argv[1]
op_type = sys.argv[2].lower()[:1]
val = sys.argv[3]

addr = (host, UDP_PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if op_type == 'w': # write
    req = hdr.pack(OP_WRITE, val)
else: # read
    req = hdr.pack(OP_READ, val)

s.sendto(req, addr)
res, addr2 = s.recvfrom(1024)

op_type, val = hdr.unpack(res)

print val
