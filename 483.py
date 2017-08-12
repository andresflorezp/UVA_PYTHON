import sys
def sol():
    val=0
    while val!="":
        container=[]
        val=sys.stdin.readline().strip().split()
        if len(val)==0:
            break
        for i in val:
            container.append(i[::-1])

        print(" ".join(container))
        del container
        container=[]

sol()
