import string
import sys
import io
import struct
import binascii

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
message += b'\x00' * ((56 - (msg_len + 1) % 64) % 64) #pad zeroes
message += struct.pack(b'>Q', msg_len_b) #usigned long long (8bytes 64 bit) Big Endian
#message should be message len in bits + 1 + zeroes + 64 bit representation of length  = 512

print bin(int(binascii.hexlify(message),16))
print len(message)*8
#print b'\x80'
SHAfile.close
sys.exit()
