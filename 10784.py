from math import *
import sys
def sol():
    val=1
    count=1
    while val!=0:
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        total=(val*2+9/4)
        raiz=sqrt(total)+3/2
        raiz=int(raiz)
        print("Case {}: {}".format(count,raiz+1))
        count+=1
              
sol()
print()
