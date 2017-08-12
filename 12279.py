import sys
def sol():
    val=1
    dates=0
    count=0
    conta=1
    while val!=0:
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        dates=list(map(int,sys.stdin.readline().strip().split()))
        for i in dates:
            if i!=0:
                count+=1
            else:
                count-=1

        print("Case {}: {}".format(conta,count))
        conta+=1
        count=0

sol()
        
