# Purpose
Use the switch registers to rewrite packet payload. User sends a packet with
custom header that has two fields. The first header field indicates whether packet
is a `read` type or a `write` type. The second field is the packet payload.

If packet is a `write` type, we save its payload (say, `fooo`) for future packets.
Every subsequent `read` packet's payload (say, `barr`) is going to be replaced
with the payload of the previous `write` packet (i.e., `fooo`). If user sends
another `write` packet (say, with payload `foo1`) every `read` packet that follows
gets its payload replaced with `foo1`.

Note that the length of the payload is important here as it corresponds to the
length of the second field (`bit<32>`) in the custom header (`myHdr_t`).
Therefore, all packet payloads must be exactly 4 characters long (not even 3).

# Run
Install `p4app` tool as instructed [here](https://github.com/p4lang/p4app).
Run `sudo p4app run payload-swap.p4cap` on a single terminal. The successfull
output should be as follows
```
$ cd hackathons
$ sudo p4app run payload-swap.p4cap
> python /p4app/main.py 
sent a write packet with payload *fooo* and received: fooo

sent a read packet with payload *barr* and received: fooo

sent a write packet with payload *bazz* and received: fooo

sent a write packet with payload *foo1* and received: foo1

sent a read packet with payload *barr* and received: foo1

Quit.
```

# Credits
Project is developed in [March 2019 P4 hackathon](https://p4.org/events/2019-03-01-nsdi/).
This code is mostly based on 
[registers](https://github.com/p4lang/p4app/tree/rc-2.0.0/examples/registers.p4app)
example provided in p4app examples. Note the `rc-2.0.0` branch (not `master`).
This example is developed by [Nodir Kodirov](https://github.com/knodir) with a 
big help from P4 hackathon organizers and volunteers, including
[Robert Soulé](https://www.inf.usi.ch/faculty/soule/) and
[Noa Zilberman](https://www.cl.cam.ac.uk/~nz247/).
