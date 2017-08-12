import sys
def sol():
    case=int(sys.stdin.readline().strip())
    for j in range(case):
        while True:
            try:
                val=sys.stdin.readline().strip().split()
                if len(val)==0:
                    break
                re=" "
                for i in val:
                    i=i.replace("3","E")
                    i=i.replace("0","O")
                    i=i.replace("1","I")
                    i=i.replace("4","A")
                    i=i.replace("9","P")
                    i=i.replace("5","S")
                    i=i.replace("8","B")
                    i=i.replace("7","T")
                    i=i.replace("2","Z")
                    i=i.replace("6","G")
                    re+=i+" "
                print(re[1:-1])
            except:
                break

        if j+1!=case:
            print()
    
sol()
                    
    
