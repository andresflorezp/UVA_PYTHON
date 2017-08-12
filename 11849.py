import sys
def main():
    case=0
    container=set()
    container2=set()
    val=0
    while True:
        case=[int(x) for x in sys.stdin.readline().strip().split()]
        if case == [0,0]:
            break
        for i in range(case[0]):
            val=int(sys.stdin.readline().strip())
            container.add(val)

        for i in range(case[1]):
            val=int(sys.stdin.readline().strip())
            container2.add(val)
        print(len(container & container2))
        del container
        container=set()
        del container2
        container2= set()
main()
        
