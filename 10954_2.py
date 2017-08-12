import sys
import queue
def main():
    val=1
    priority=queue.PriorityQueue()
    total=0
    while True:
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        for x in sys.stdin.readline().strip().split():
            priority.put(int(x))
        while True:
            
            val1=priority.get()
            if priority.empty():
        
                print(total)
                break
            val2=priority.get()
            suma=val1+val2
            priority.put(suma)
            total+=suma
        total=0
main()
        
        
