from math import *
import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        r=0
        val=int(sys.stdin.readline().strip())
        for i in range(1,val+1):
            r+=(log(i,10))  
        print(int(r)+1)
            
sol()
