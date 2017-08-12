import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    dates=0
    countup=0
    countdown=0
    count=1
    for i in range(case):
        dates=int(sys.stdin.readline().strip())
        val=list(map(int,sys.stdin.readline().strip().split()))
        for i in range(len(val)-1):
            if val[i]<val[i+1]:
                countup+=1
            elif val[i]>val[i+1]:
                countdown+=1
        print("Case {}: {} {}".format(count,countup,countdown))
        count+=1
        countup=0
        countdown=0
sol()
