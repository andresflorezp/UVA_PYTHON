import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val=int(sys.stdin.readline().strip())
        m=(val*567)//9
        n=m+7492
        o=(n*235)//47
        p=o-498
        l=str(p)
        print(l[-2])
sol()
        
