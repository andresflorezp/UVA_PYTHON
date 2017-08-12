import sys
#NOTA
#Arreglar numero de ceros
re=[]
def numberToBase(n):
    global re
    count=0
    if n==0:
        return ["0"]
    
    while n!=1:
        re.append(str(n%3))
        if n%3==0:
            count+=1
        else:
            count=0
        if count==4:
            re=re[:-4]
            return re[::-1]
            break
        
        n=n//3
    re.append("1")
    return re[::-1]
    
   
    
val=0
while val>=0:
    val=int(sys.stdin.readline().strip())
    if val<0:
        break
    print("".join(numberToBase(val)))
    del re
    re=[]
    

