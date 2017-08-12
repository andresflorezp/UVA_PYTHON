import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    conta=1
    for i in range(case):
        val=sys.stdin.readline().strip().split()
        if len(val)==2:
            print("Case {}: {}".format(conta,format(int(val[0])*0.5),'.2f'))
        else:
            print("Case {}: {}".format(conta,format(int(val[0])*0.5+int(val[2])*0.05),'.2f'))
        conta+=1

sol()
