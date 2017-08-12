import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    M=0
    F=0
    for i in range(case):
        val=sys.stdin.readline().strip().split()
        for i in  val:
            M+=i.count("M")
            F+=i.count("F")

        if len(val)==1 or M!=F:
            print("NO LOOP")
        else:
            print("LOOP")
        M=0
        F=0
        


sol()
        
