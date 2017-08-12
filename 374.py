import sys
def sol():
    B=0
    P=0
    M=0
    blank=0
    while True:
        B=sys.stdin.readline().strip()
        if B=="":
            break
        P=int(sys.stdin.readline().strip())
        M=int(sys.stdin.readline().strip())
        print((int(B)**P)%M)
        blank=sys.stdin.readline().strip()
        

sol()
