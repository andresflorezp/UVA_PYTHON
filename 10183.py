import sys
def fibo(a,b):
    count=0
    temp=1
    temp2=2
    for i in range(2,b+1):
        temp,temp2=temp+temp2,temp
        if a<=temp<=b:
            count+=1

    return count

def main():
    val=[0]
    while True:
        if val==[0,0]:
            break
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        print(fibo(val[0],val[1]))

main()
        
