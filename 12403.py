import sys
def sol():
    case=int(sys.stdin.readline().strip())
    val=0
    count=0
    for i in range(case):
        val=sys.stdin.readline().strip().split()
        if val[0]=="report":
            print(count)
        else:
            count+=int(val[1])

sol()
