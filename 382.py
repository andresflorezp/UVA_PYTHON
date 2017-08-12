import sys
def divisores(v):
    container=[]
    for i in range(1,v):
        if v%i==0:
            container.append(i)

    if sum(container)==v:
        return "PERFECT"
    elif sum(container)<v:
        return "DEFICIENT"
    elif sum(container)>v:
        return "ABUNDANT"


def main():
    val=[int(x) for x in sys.stdin.readline().strip().split()]
    val.pop(-1)
    print("PERFECTION OUTPUT")
    for i in val:
        if len(str(i))==5:
            print("{}  {}".format(i,divisores(i)))
        if len(str(i))==4:
            print(" {}  {}".format(i,divisores(i)))
        if len(str(i))==3:
            print("  {}  {}".format(i,divisores(i)))
        if len(str(i))==2:
            print("   {}  {}".format(i,divisores(i)))
        if len(str(i))==1:
            print("    {}  {}".format(i,divisores(i)))
        

    print("END OF OUTPUT")
main()

