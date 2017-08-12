from math import *
import sys
def operar(N,M):
    c=factorial(N)/(factorial(N-M)*factorial(M))
    return int(c)
def main():
    val=[10]
    while True:
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        if val==[0,0]:
            break
        print("{} things taken {} at a time is {} exactly.".format(val[0],val[1],operar(val[0],val[1])))

main()
        
