import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val=list(map(int,sys.stdin.readline().strip().split()))
        temp=str(val[0])
        temp2=str(val[1])
        temp=int(temp[::-1])
        temp2=int(temp2[::-1])
        total=temp+temp2
        total=str(total)
        total=int(total[::-1])
        print(total)
sol()
