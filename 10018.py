import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val=sys.stdin.readline().strip()
        count=0
        time=0
        while val!=val[::-1]:
            count=int(val)+int(val[::-1])
            val=str(count)
            time+=1
        print(time,val)
        count=0
        time=0
sol()
        
    
