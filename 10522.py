import sys
def veri(l):
    veri=True
    if l[0]+l[1]<=l[2]:
        veri=False

    return veri



def main():
    count=int(sys.stdin.readline().strip())
    val=0
    while True:
        val=[float(x) for x in sys.stdin.readline().strip().split()]
        if len(val)==0:
            break
        container=sorted(val)
        verif=veri(container)
        if not verif:
            print("These are invalid inputs!")
        else:
            s=sum(container)/2
            area=(s*(s-container[0])*(s-container[1])*(s-container[2]))**(1/2)
            print(area)

    
main()
