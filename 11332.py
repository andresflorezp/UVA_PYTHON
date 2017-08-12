import sys
def sol(n):
    count=0
    value=n
    while len(value)!=1:
        for i in value:
            count+=int(i)
        value=str(count)
        count=0
    return value





def main():
    val=9
    while val!="0":
        
        val=sys.stdin.readline().strip()
        if val=="0":
            break
        print(sol(val))
main()


    
