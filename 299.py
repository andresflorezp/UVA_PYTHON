import sys
def burbuja(l):
    count=0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
                count+=1
    return count



def sol():
    val=0
    data=0
    case=int(sys.stdin.readline().strip())
    for i in range(case):
        val=sys.stdin.readline().strip()
        data=list(map(int,sys.stdin.readline().strip().split()))
        print("Optimal train swapping takes {} swaps.".format(burbuja(data)))

sol()

        
        
