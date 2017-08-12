import sys
def fibo(n):
    fi1=0
    fi2=1
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(n):
        temp=fi2
        fi2=fi1+fi2
        fi1=temp

    return temp
        


def sol():
    val=0
    while True:
        val=sys.stdin.readline().strip()
        if val=="":
            break
        print("The Fibonacci number for {} is {}".format(val,fibo(int(val))))

sol()
