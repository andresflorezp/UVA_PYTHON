from math import *
import sys
def main():
    val=0
    while True:
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        if val==[0,0,0]:
            break
        val=sorted(val)
        if hypot(val[0],val[1])!=val[2]:
            print("wrong")

        else:
            print("right")
            
            
main()
    
    
    
