import sys
#"x(1)=x(0)-f(x)/f'(x)"
#f(x)=x^2
#x(0)=0.5
def raiz(m):
    n=1
    x=1
    while n<=100:
        y=x-(((x**2)-m)/(2*x))
        x=y
        n=n+1
    return(x)

def main():
    case=int(sys.stdin.readline().strip())
    blank=0
    val=0
    
    for i in range(case):
        blank=sys.stdin.readline().strip()
        val=int(sys.stdin.readline().strip())
        print(int(raiz(val)))
        if i+1==case:
            break
        print()
        
main()
    
