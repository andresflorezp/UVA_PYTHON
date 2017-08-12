import sys
def sol():
    case=1
    while case!=0:
        case=int(sys.stdin.readline().strip())
        container=[]
        veri=True
        for i in range(case):
            val1=int(sys.stdin.readline().strip())
            if len(container)>=1 and (val1-container[-1]>200  or (val1 in container))or val1>1422:
                veri=False
            
            container.append(val1)
        if i+1==case and veri==True:
            print("POSSIBLE")

        elif i+1==case and veri==False:
            print("IMPOSSIBLE")
                

        del container
        container=[]
sol()

     
            
            

