import sys
case = int(sys.stdin.readline().strip())
for i in range(case):
    blank=sys.stdin.readline().strip()
    container=[int(x) for x in sys.stdin.readline().strip().split()]
    container2=sys.stdin.readline().strip().split()
    for h,j in sorted(zip(container,container2)):
        print(j)
    

    if i+1!=case:
        print()

    
    
