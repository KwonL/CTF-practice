# core

We can use core file with GDB.

`gdb -q ./print_flag ./core`

Then, disassemble and analyze code. There will be flag in (0x539 * 4 + 0x804a080)

`picoCTF{e52f4714963eb207ae54fd424ce3c7d4}`