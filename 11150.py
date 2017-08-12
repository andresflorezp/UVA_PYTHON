import sys
def completar(x):
    conta=0
    while x%3!=0:
        x+=1
        conta+=1
    return (x,conta)
    
def sol(n,r):
    count = 0
    while True:
        if n==0:
            break
        count+=n
        n=n//3
        
    return count - r



def main():
    case = 0
    while True:
        case = sys.stdin.readline().strip()
        if case == "":
            break
        elif case == "1":
            print (1)
        
        else:
            case = int(case)
            guarda1,guarda2 = completar(case)
            print(sol(guarda1,guarda2))
    
main()    
