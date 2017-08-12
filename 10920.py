import sys
from math import *    
def anillo(val):
    raiz = sqrt(val)
    if raiz * raiz ==val and raiz%2==1:
        if raiz%2==1:
            raiz+=2
        else:
            raiz+=1
    i = raiz // 2
    j = raiz // 2
    if raiz *raiz!=1:
        group = (raiz*raiz-val) / (raiz-1)
    print(raiz)
    print(group)
    
        
        
    


def main():
    while True:
        case = [int(x) for x in sys.stdin.readline().strip().split()]
        if case == [0,0]:
            break
        anillo(case[1])
main()
