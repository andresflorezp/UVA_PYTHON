import sys
def sol(container):
    descartadas=[]
    while len(container)!=1:
        descartadas.append(container.pop(0))
        container.append(container.pop(0))
    return descartadas,container
def main():
    val=1
    while True:
        val = int(sys.stdin.readline().strip())
        if val==0:
            break
        if val==1:
            print("Discarded cards:")
            print("Remaining card: {}".format(1))
        else:
            container=[i for i in range(1,val+1)]
            des,res=sol(container)
            print("Discarded cards: {}".format(", ".join(map(str,des))))
            print("Remaining card: {}".format(res[0]))
main()
        
    
