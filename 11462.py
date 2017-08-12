import sys
def sol():
    val=1
    case=0
    while val!=0:
        
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        case=list(map(int,sys.stdin.readline().strip().split()))
        a=sorted(case)
        print(" ".join(map(str,a)))
sol()
        
