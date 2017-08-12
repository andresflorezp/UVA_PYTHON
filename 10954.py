import sys
import heapq
def main():
    val=1
    total=0
    while True:
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        container=[int(x) for x in sys.stdin.readline().strip().split()]
        while True:
            try:
                heapq.heapify(container)
                guarda1=heapq.nsmallest(50, container)
                container=container[50:]
                guarda1=sorted(guarda1)
                suma=guarda1[0]+guarda1[1]
                total+=guarda1[0]+guarda1[1]
                container=guarda1+container
                del container[0]
                del container[0]
                heapq.heappush(container,suma)
            except:
                print(total)
                break
        del container
        container=[]
        total=0
        suma=0
main()
        
        
        
