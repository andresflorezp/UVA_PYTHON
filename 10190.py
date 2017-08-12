import sys
def sol():
    val=0
    container=[]
    while True:
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        if len(val)==0:
            break
        value=val[0]
        container.append(val[0])
        while value!=1:

            if value%val[1]==0 or (value==0 or val[1]==0 or val[1]==1 or value ==1):
                container.append(value//val[1])
                value=value//val[1]
            elif value%val[1]!=0 or value==0 or val[1]==0 or val[1]==1 or value ==1:
                print("Boring!")
                del container
                container=[]
                break
            
        if len(container)>=1:
            print(" ".join(map(str,container)))
        del container
        container=[]

sol()
        
