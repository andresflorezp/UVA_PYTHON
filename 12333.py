import sys
def fibonacci(n):
    temp1=1
    temp2=1
    count=0
    while count<n-1:
        temp1,temp2=temp1+temp2,temp1
        count+=1
    return(temp1)
while True:
    k=int(sys.stdin.readline().strip())
    val=0
    long=len(str(k))
    while True:
        guarda=str(fibonacci(val))
        if str(k) == guarda[:long]:
            print(val)
            break
        val+=1
