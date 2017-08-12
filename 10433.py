import sys
def sol():
    val=0
    while True:
        val=sys.stdin.readline().strip()
        if val=="":
            break
        long=len(val)
        proces=int(val)**2
        proces=str(proces)
        if int(proces)==0 or int(proces)==1:
            print("Not an Automorphic number.")
        elif proces[-1*long:]==val:
            print("Automorphic number of {}-digit.".format(long))
        else:
            print("Not an Automorphic number.")
sol()
