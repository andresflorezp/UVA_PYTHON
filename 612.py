import sys
def burbuja(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
def main():
    case=int(sys.stdin.readline().strip())
    blank=sys.stdin.readline().strip()
    val=0
    container=[]
    for i in range(case):
        col = [int(x) for x in sys.stdin.readline().strip().split()]
        for j in range(col[1]):
            val = sys.stdin.readline().strip()
            container.append(val)

        container = burbuja(container)
        for i in container:
            print(i)

        print()
        del container
        container=[]

main()
            

            
        
