import sys
def sol():
    val=0
    while val!="":
        val=sys.stdin.readline().strip()
        if val=="":
            break
        print(val)

sol()
