import sys
case=int(sys.stdin.readline().strip())
temp=0
temp2=0
for i in range(case):
    temp=int(sys.stdin.readline().strip())
    temp2=int(sys.stdin.readline().strip())
    l=[i for i in range(temp,temp2+1) if (i%2)]
    print("Case {}: {}".format(i+1,sum(l)))

    

    
        
