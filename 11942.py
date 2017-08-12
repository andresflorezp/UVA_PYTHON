import sys
def creciente(l):
    veri=True
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            veri=False
    return veri
    

def decreciente(l):
    veri=True
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            veri=False
    return veri



def main():
    case=int(sys.stdin.readline().strip())
    val=0
    print("Lumberjacks:")
    for i in range(case):
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        if creciente(val) or decreciente(val):
            print("Ordered")
        elif creciente(val)==False and decreciente(val)==False:
            print("Unordered")
        
main()
