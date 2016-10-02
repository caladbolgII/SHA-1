import string
import sys
import io
import struct
import binascii

def leftrot(n,b):
   return((n<<b) | (n>>(32-b)))& 0xffffffff

h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476
h4 = 0xC3D2E1F0

SHAfile = open("pushmo.cia" , "rb")
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
for i in range(0, len(message), 64):
    w = [0]*80
    for g in range(16):
        w[g] = struct.unpack(b'>I', message[i + g*4:i + g*4 + 4])[0]
#    break chunk into sixteen 32-bit big-endian words
#Extend the sixteen 32-bit words into eighty 32-bit words:
    for h in range(16,80):
        w[h] =  leftrot(w[h-3] ^ w[h-8] ^ w[h-14] ^ w[h-16],1)
#initialize hash for chunk
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    for i in range(80):
        if 0 <= i <= 19:
            # Use alternative 1 for f from FIPS PB 180-1 to avoid ~
            f = d ^ (b & (c ^ d))
            k = 0x5A827999
        elif 20 <= i <= 39:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif 40 <= i <= 59:
            f = (b & c) | (b & d) | (c & d)
            k = 0x8F1BBCDC
        elif 60 <= i <= 79:
            f = b ^ c ^ d
            k = 0xCA62C1D6

        temp = (leftrot(a, 5) + f + e + k + w[i]) & 0xffffffff
        e = d
        d = c
        c = leftrot(b, 30)
        b = a
        a = temp

    # sAdd this chunk's hash to result so far:
    h0 = (h0 + a) & 0xffffffff
    h1 = (h1 + b) & 0xffffffff
    h2 = (h2 + c) & 0xffffffff
    h3 = (h3 + d) & 0xffffffff
    h4 = (h4 + e) & 0xffffffff

    # Produce the final hash value (big-endian):
print '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
#print bin(int(binascii.hexlify(message),16))
#print len(message)*8
#print b'\x80'
SHAfile.close
sys.exit()
