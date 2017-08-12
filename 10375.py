import sys
from math import *
def sol():
    val=[1]
    while len(val)!=0:
        val=list(map(int,sys.stdin.readline().strip().split()))
        m=factorial(val[0])/(factorial(val[0]-val[1])*factorial(val[1]))
        m2=factorial(val[2])/(factorial(val[2]-val[3])*factorial(val[3]))
        a=(m/m2)
        print(a)
        print("{0:.1f}".format(a))

sol()
        
