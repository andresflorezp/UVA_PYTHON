import sys
def sol(n):
    numero1="one"
    numero2="two"
    numero3="three"
    count1=0
    count2=0
    count3=0
    for i,j,k,l in zip(n,numero1,numero2,numero3):
        if i==j:
            count1+=1
        if i==k:
            count2+=1
        if i==l:
            count3+=1
    maximo=max(count1,count2,count3)
    if maximo==count1:
        return 1
    elif maximo==count2:
        return 2
    else:
        return 3


def main():
    case=int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val=sys.stdin.readline().strip()
        print(sol(val))

main()
        
