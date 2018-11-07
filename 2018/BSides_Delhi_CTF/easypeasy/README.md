# Easy Peasy

We can call syscall by setting some registers. 

Just execute /bin/sh by call read, execve. 

execve will not called because that is not allowed number. 

After 30seconds, SIGALRM will wakeup execve!

`flag{0p3n_re4d_wr1te}`