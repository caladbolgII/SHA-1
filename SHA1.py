import string
import sys


SHAfile = open("hello.txt" , "r+")
#SHAfile.write("Hello Planet")
string = SHAfile.read();
print string
SHAfile.close
sys.exit()
