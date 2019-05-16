#!/usr/bin/python
from pwn import *

context.log_level = 'debug'
context.terminal = ['tmux', 'split', '-h']

HOST = ''
PORT = 0
# conn = remote(HOST, PORT)
conn = process('')

# Exploit here

conn.interactive()