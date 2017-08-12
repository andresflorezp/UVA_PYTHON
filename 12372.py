import sys
def sol():
    case=int(sys.stdin.readline().strip())
    count=1
    val=0
    for i in range(case):
        val=list(map(int,sys.stdin.readline().strip().split()))
        if val[0]<=20 and val[1]<=20 and val[2]<=20:
            print("Case {}: good".format(count))
        else:
            print("Case {}: bad".format(count))
        count+=1
sol()
            
