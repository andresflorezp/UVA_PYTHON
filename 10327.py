import sys
def burbuja(l):
    count=0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
                count+=1
    return count
def main():
    case=0
    while True:
        case = sys.stdin.readline().strip()
        if case =='':
            break
        val =[int(x) for x in sys.stdin.readline().strip().split()]
        print("Minimum exchange operations : {}".format(burbuja(val)))


main()
            
