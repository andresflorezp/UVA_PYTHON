import sys
def orden(l):
    count=0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                count+=1

    return count
                
def sol():
    val=1
    count=1
    while val!=0:
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        dates=[int(x) for x in sys.stdin.readline().strip().split()]
        print("Set #{}".format(count))
        print("The minimum number of moves is {}.".format(orden(dates)))
        count+=1

sol()

        
        
