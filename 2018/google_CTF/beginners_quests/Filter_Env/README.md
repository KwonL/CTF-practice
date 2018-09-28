# Filter Env

This program seems to filtering vulnerable enviromental vars and execute /usr/bin/id

So, I search for vulnerable enviromental vars and find this post :

http://umbum.tistory.com/128

If i can modify LD_PRELOAD, then i can inject my_hook.so and execute command.

We can exploit filter_env function by just typing LD_PRELOAD=/tmp/my_hook.so twice..

I compiled 'hook.c' with following command

```
gcc -shared -o hook.so -fPIC hook.c
```

And send it over nc, using base64 encoding (Just sending raw file does not work. I don't know why..but just encoding it to txt file and decode).

CTF{H3ll0-Kingc0p3}