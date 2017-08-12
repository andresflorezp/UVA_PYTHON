import sys
def main():
    case = int(sys.stdin.readline().strip())
    val=0
    container=[]
    dx=[]
    dy=[]
    for i in range(case):
        val=list((sys.stdin.readline().strip()))
        for i in val:
            if i!=" ":
                container.append(int(i))

        count=0
        for i in range(len(container)-2,-1,-2):
            dx.append(str(container[i]*2))


        for j in dx:
            for h in j:
                count+=int(h)
        
        count2=0
        for i in range(len(container)-1,0,-2):
            dy.append(container[i])
        count2=sum(dy)
        
        
        if (count2+count)%10==0:
            print("Valid")
        else:
            print("Invalid")
        
        
            

        del container
        container=[]
        del dx
        dx=[]
        del dy
        dy=[]
        
        
            

main()
                 
        
        
