import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val=list(map(int,sys.stdin.readline().strip().split()))
        a=val[1]
        b=val[0]
        c=(a-b)//2
        d=c+b
        if(c < 0 or d<0):
            print("impossible")
        else:
            
            print("{} {}".format(d,c));
sol()
        
        
