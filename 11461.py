import sys
count=0
veri=1
while True:
    case=[int(x) for x in sys.stdin.readline().strip().split()]
    if case[0]==0 and case[1]==0:
        break
    for i in range(case[0],case[1]+1):
        if i**2<=case[1]:
            count+=1
        elif i**2>case[1]:
            print(count)
            count=0
            break
    
