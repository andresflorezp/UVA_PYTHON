import sys
gen=[0 for i in range(10)]
cuenta=[str(i) for i in range(10)]
def sol():
    global gen
    global cuenta
    val=0
    count=0
    case=int(sys.stdin.readline().strip())
    for i in range(case):
        val=sys.stdin.readline().strip()
        if val=="":
            break
        for j in range(1,int(val)+1):
            for i in range(len(cuenta)):
                cambio=str(j)
                count=cambio.count(cuenta[i])
                gen[i]+=count

        print(" ".join(map(str,gen)))
        del gen
        gen=[0 for i in range(10)]
        
sol()
            
        

