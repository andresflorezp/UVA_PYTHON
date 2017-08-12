import sys
def minimo(lista):
    a=lista[0]
    b=lista[1]
    return min(a,b)
def maximo(lista):
    a=lista[0]
    b=lista[1]
    return max(a,b)


def main():
    cadena=0
    count=1
    while True:
        cadena=sys.stdin.readline().strip()
        if cadena=="":
            break
        case=int(sys.stdin.readline().strip())
        val=0
        print("Case {}:".format(count))
        for i in range(case):
            val=[int(x) for x in sys.stdin.readline().strip().split()]
            i=minimo(val)
            j=maximo(val)
            pedazo=cadena[i:j+1]
            if pedazo.count("0")==len(pedazo) or pedazo.count("1")==len(pedazo):
                print("Yes")
            else:
                print("No")
        count+=1
main()
    
