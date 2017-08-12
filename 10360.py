import sys
def cuan(val1,val2):
    lis=[chr(i) for i in range(97,123)]
    container1=[]
    container2=[]
    for i in val1:
        container1.append(lis.index(i)+1)
    for i in val2:
        container2.append(lis.index(i)+1)
    total1=str(sum(container1))
    total2=str(sum(container2))
    count1=0
    count2=0
    while len(total1)!=1:
        if len(val1)==1:
            break
        for i in total1:
            count1+=int(i)

        total1=str(count1)
        count1=0
    while len(total2)!=1:
        if len(val2)==1:
            break
        for i in total2:
            count2+=int(i)

        total2=str(count2)
        count2=0
    return total1,total2
    
        
    
    
  
    


def sol():
    val1=0
    val2=0
    while val1!="":
        val1=sys.stdin.readline().strip()
        val1=val1.lower()
        if val1=="":
            break
        val2=sys.stdin.readline().strip()
        val2=val2.lower()
      
        alma=list(cuan(val1,val2))
        total=round((int(alma[1])/int(alma[0]))*100,2) 
        print("{} %".format(format(total,".2f")))
        

sol()

        
        
