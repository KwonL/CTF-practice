# Message of the Day

Using checksec, we can get following result

```
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      No PIE (0x400000)
```

umm,,there is no canary and aslr..so we can use buffer overflow.

In option 2, motd get user input and stack size is 0x100. Including rbp address, I send 0x108 * 'A' and can modify return address.

CTF{m07d_1s_r3t_2_r34d_fl4g}