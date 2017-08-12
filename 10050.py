import sys
def sol(dias,h):
    veri=[]
    for i in range(len(h)):
        for j in range(len(dias)):
            mod = (dias[j]) % 7
            if dias[j]%h[i]==0 and dias[j] not in veri and mod != 0 and mod != 6:
                veri.append(dias[j])

    return len(veri)
    
    
def main():
    case = int(sys.stdin.readline().strip())
    hartals=[]
    for i in range(case):
        dias=[i for i in range(1,int(sys.stdin.readline().strip())+1) if not i%7==0]
            
        case2=int(sys.stdin.readline().strip())
        for i in range(case2):
            val=int(sys.stdin.readline().strip())
            hartals.append(val)
        print(sol(dias,hartals))
        del hartals
        hartals=[]
main()  

