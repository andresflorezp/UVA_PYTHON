import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    cuan=0
    for i in range(case):
        val=sys.stdin.readline().strip()
        cuan= list(map(int,sys.stdin.readline().strip().split()))
        maxi=0
        mini=99
        for i in cuan:
            if maxi<=i:
                maxi=i
            if mini>=i:
                mini=i

        print((maxi-mini)*2)

sol()
