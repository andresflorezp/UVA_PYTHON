import sys
case=int(sys.stdin.readline().strip())
for i in range(case):
    val=sys.stdin.readline().strip()
    count=1
    ele=1
    while True:
        for i in str(ele):
            count*=int(i)
        if count==int(val):
            print(ele)
            count=1
            break
        elif count>int(val):
            print(-1)
            count=1
            break
        
        ele+=1
        count=1
    

        


    
