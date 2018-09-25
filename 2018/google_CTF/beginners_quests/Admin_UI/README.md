# Admin UI

Simply travel over file path
../../../../../......./proc/self/cmdline notify that this program's name is ./main
so we can dump main

And ./main read some flag from file name 'flag'

so, just print out by entering ../flag

CTF{I_luv_buggy_sOFtware}


# Admin UI 2

We get main binary at Admin UI 1

There is several string at end of file. And I can notice there are several messages.
I'm searching for that messages, and find authenticating point. And there are some bytes.

0x98a8b093bc819384

0x83b5a8b094b4a697

0xb5a2b3b3a28598bd

0x98f698a9f3afb398

0xf8ac

186


I think this is password, but can not convert it directly.
I find some code that xor something with 0xffffffc7. And can notice this is hashing.

finally get password! 

CTF{Two_PasSworDz_Better_th4n_1_k?}

