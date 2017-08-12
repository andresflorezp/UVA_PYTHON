import sys
from math import *
def sol():
    val=0
    while True:
        val=sys.stdin.readline().strip()
        if val=="":
            break
        temp=str(factorial(int(val)))
        for i in range(len(temp)-1,0,-1):
            if temp[i]!=0:
                print(temp[i])
                break

sol()
