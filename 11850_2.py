import sys
def sol():
    case=1
    while case!=0:
        try:
            case=int(sys.stdin.readline().strip())
            if case==0:
                break
            else:
                container=[]
                for i in range(case):
                    temp=int(sys.stdin.readline().strip())
                    container.append(temp)
                veri=True
                container=sorted(container)
                if 1422-container[case-1]>100:
                    veri=False
                container2=[]
                for i in range(1,len(container)-1):
                    if container[i]-container[i-1]>200 or (container[i] in container2):
                        veri=False
                    container2.append(container[i])
                if veri:
                    print("POSSIBLE")
                else:
                    print("IMPOSSIBLE")
                del container
                del container2
                container=[]
                container2=[]
        except:
            break
        
sol()
            
            
        
