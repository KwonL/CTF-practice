#!/usr/bin/python
from pwn import *


def add() :
    p.sendlineafter("> ", "M")

    return


p = process('./babyheap')

p.sendlineafter("> ", "M")
p.sendlineafter("> ", '248')
p.sendafter("> ", 'fisrt')