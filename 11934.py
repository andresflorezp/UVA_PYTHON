import sys
def sol():
    case=0
    while case!=[0,0,0,0,0]:
        case =[int(x) for x in sys.stdin.readline().strip().split()]
        if case==[0,0,0,0,0]:
            break
        count=0
        for i in range(case[4]+1):
            if (case[0]*(i)**2+case[1]*i + case[2])%case[3]==0:
                count+=1

        print(count)

sol()
    
