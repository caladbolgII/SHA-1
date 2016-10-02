import string
import sys
import io
import struct
import binascii
#def leftrot(n,b)
h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0
SHAfile = open("hello.txt" , "rb")
message= SHAfile.read()
    #arg = io.BytesIO(SHAfile)
msg_len = len(message)
msg_len_b = msg_len*8
message += b'\x80' #pad 1.  by adding 0x80 if message length is a multiple of 8 bits accdg to wikipedia
#message += b'\x00' * ((448 % 512) - (msg_len_b + 1)) #pad zeroes why isnt this working? how to solve congruence
message += b'\x00' * ((56 - (msg_len + 1) % 64) % 64)
message += struct.pack(b'>Q', msg_len_b) #usigned long long (8bytes 64 bit) Big Endian
#message should be message len in bits + 1 + zeroes + 64 bit representation of length  = 512
#range([start], stop[, step])
#for i in range(0, msg_len, 64):
#    w = [0]*80
#    for x in range(16)
#        w[x] = struct.pack(b'>I', message[i + x*4:i + x*4 + 4])[0])
#    break chunk into sixteen 32-bit big-endian words
#Extend the sixteen 32-bit words into eighty 32-bit words:
#for k from 16 to 79
#    w[k] =  leftrot(w[k-3] ^ w[k-8] ^ w[k-14] ^ w[k-16],1)
#initialize hash for chunk
#a = h0
#b = h1
#c = h2
#d = h3
#e = h4

print bin(int(binascii.hexlify(message),16))
print len(message)*8
#print b'\x80'
SHAfile.close
sys.exit()
