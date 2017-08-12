import sys
def sol():
    B=0
    P=0
    M=0
    while True:
        B=int(sys.stdin.readline().strip())
        P=int(sys.stdin.readline().strip())
        M=int(sys.stdin.readline().strip())
        blank=sys.stdin.readline().strip()
        print((B**P)%M)
        

sol()
    
