import sys
import queue
def main():
    priority=queue.PriorityQueue()
    while True:
        val=sys.stdin.readline().strip().split()
        if val[0]=="#":
            break
        priority.put((int(val[2]),int(val[1]),int(val[2])))
    
    case=int(sys.stdin.readline().strip())
    for i in range(case):
        guarda=priority.get()
        suma=guarda[0]+guarda[2]
        val1=guarda[1]
        val2=guarda[2]
        priority.put((suma,val1,val2))
        print(val1)
main()
        
