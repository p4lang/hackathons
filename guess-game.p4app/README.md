# Purpose
Play number guess game with the switch dataplane. First we generate a secret
number randomly and write it to switch. We then ask the user to enter a number
to guess the secret number. Here is how it works in a high level.

User sends a packet with custom header that has two fields. The first header
field indicates whether packet is a `read` type or a `write` type. The second
field is the packet payload. The secret number is written with a packet with
the `write` type. We save its payload (say, 8) as the secret number.
Every following guess numbers are sent with `read` type packet. If the guess number
matches the secret number we congratulate the user and end the game. Otherwise,
we hint the user if the secret number is smaller or the larger than user
entered guess number.

# Run
Install `p4app` tool as instructed [here](https://github.com/p4lang/p4app).
Run `sudo p4app run guess-game.p4app` on a single terminal. The successfull
output should be as follows
```
$ cd hackathons
$ sudo p4app run guess-game.p4app
> python /p4app/main.py 
wrote secret number 8 to switch dataplane
Pretend that you do not know the secret number and try to guess it. Start now.
Enter an integer from 1 to 9: 1
str_to_send = ./send.py 10.0.0.2 read 1
Hidden number is larger
Enter an integer from 1 to 9: 5
str_to_send = ./send.py 10.0.0.2 read 5
Hidden number is larger
Enter an integer from 1 to 9: 9
str_to_send = ./send.py 10.0.0.2 read 9
Hidden number is smaller
Enter an integer from 1 to 9: 8
str_to_send = ./send.py 10.0.0.2 read 8
Congrats!
Game over, bye.
OK
```

# Credits
Project is developed in [March 2019 P4 hackathon](https://p4.org/events/2019-03-01-nsdi/).
This code is built on top of [payload-swap](../payload-swap.p4app) example that
is mostly based on 
[registers](https://github.com/p4lang/p4app/tree/rc-2.0.0/examples/registers.p4app)
example provided in p4app examples.
This example is developed by [Nodir Kodirov](https://github.com/knodir) with a 
big help from P4 hackathon organizers and volunteers, including
[Robert Soulé](https://www.inf.usi.ch/faculty/soule/) and
[Noa Zilberman](https://www.cl.cam.ac.uk/~nz247/).
