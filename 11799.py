import sys
def maximo(n):
    temp=n[0]
    for i in n:
        if i>temp:
            temp=i
    return temp



def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    count=1
    for i in range(case):
        val=list(map(int,sys.stdin.readline().strip().split()))
        print("Case {}: {}".format(count,maximo(val)))
        count+=1
sol()




