import sys
def sol():
    case=int(sys.stdin.readline().strip())
    fre=0
    ampl=0
    for i in range(case):
        blank=sys.stdin.readline().strip()
        fre=int(sys.stdin.readline().strip())
        ampl=int(sys.stdin.readline().strip())
        count=1
        for i in range(ampl):
            for i in range(ampl*2-1):
                if i <=ampl:
                    print(str(count)*count)
                    count+=1
                if i==ampl:
                    count-=2
                elif i>ampl:
                    print(str(count)*count)
                    count-=1
            
            count=1
            print()
                
sol()
            
        
