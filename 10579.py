import sys
def fib(n):
    a = 1
    b = 0
    for i in range(n):
        a, b = b, a + b
    return b


def fmemo(n):
    matriz=[1 for i in range(n+1)]
    for i in range(2,n+1):
        if i==0:
            matriz[0]=1
        elif i==1:
            matriz[1]=1
        else:
            matriz[i]=matriz[i-1] + matriz[i-2]
    return matriz[n-1]
    
def main():
    val=0
    while val!="":
        val=sys.stdin.readline().strip()
        if val=="":
            break
        print(fmemo(int(val)))
main()
