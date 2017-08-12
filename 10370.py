import sys
def operar(A,i):
    total=sum(A)
    promedio=total/i
    container=[i for i in A if i>promedio]
    long=len(container)
    val=(long*100)/i
    return val
    
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        print("{0:.3f}%".format(operar(val[1:],val[0])))
sol()
        
