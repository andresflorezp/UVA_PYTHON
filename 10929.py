import sys
def sol():
    val=1
    conta=0
    while val!=0:
        val=sys.stdin.readline().strip()
        if val=="0":
            break
        for i in range(len(val)-1):
            if i%2==0:
                conta+=-1*int(val[i])
            else:
                conta+=int(val[i])
        if conta%11==0:
            print("{} is a multiple of 11.".format(val))
        else:
            print("{} is not a multiple of 11.".format(val))
        conta=0
        
            
            
sol()
