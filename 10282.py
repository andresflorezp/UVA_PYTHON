import sys
def sol():
    diic={}
    val=[0]
    while True:
        val=sys.stdin.readline().strip().split()
        if len(val)==0:
            break
        diic[val[1]]=val[0]

    val2=0
    while True:
        try:
            val2=sys.stdin.readline().strip()
            if val2=="":
                break
            print(diic[val2])
        except KeyError:
            print("eh")
sol()
                
    
