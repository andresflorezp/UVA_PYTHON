import sys
gen=[str(i) for i in range(10)]
def sol():
    global gen
    val=0
    veri=True
    count=0
    while True:
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        if len(val)==0:
            break
        for j in range(val[0],val[1]+1):
            for i in gen:
                cambio=str(j)
                if cambio.count(i)>=2:
                    veri=False
                    break

            if veri==True:
                count+=1
            else:
                veri=True

        print(count)
        count=0
        veri=True

sol()
                

                
            
        

        
