import sys
def veri(l):
    vari=True
    for i in range(len(l)-1):
        if abs(l[i])-abs(l[i+1])>=2:
            vari = False

    return vari
         
def main():
    val=[0]
    container = []
    while True:
        val = [int(x) for x in sys.stdin.readline().strip().split()]
        if len(val) == 0:
            break
        for i in range(len(val)-1):
            container.append(abs(val[i])-abs(val[i+1]))
        if veri(container) :
            print("Jolly")
        elif not veri(container):
            print("Not jolly")
        
main()
