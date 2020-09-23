#! usr/bin/python3
import socket
print("~P.s~")
dn=input("[+] DOMAIN NAME >> ")
try:
    ip=socket.gethostbyname(dn)
except:
    print("[!]Not found...!")
else:
    print(f"{dn} <--> {ip}")

