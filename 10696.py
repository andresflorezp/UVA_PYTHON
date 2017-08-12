import sys
def f91(N):
    if N>=101:
        return N-10
    elif N<=101:
        return 91



val=1
while val!=0:
    val=int(sys.stdin.readline().strip())
    if val==0:
        break
    print("f91({}) = {}".format(val,f91(val)))
        
