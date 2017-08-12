import sys
M=[[-1 for i in range(20+1)]for j in range(20+1)]
def sol(i,j,n):
    global M
    result=M[i][j]
    if result!=-1:
        if i<j:
            for k in range(i,j):
                result=max(result,sol(i,k,n)+sol(k+1,j,n))
            return result
    if(i==n and j==1):
        return result
    else:
        max1=0
        max2=0
        if i<n:
            for k in range(i+1,n+1):
                max1=max(max1,sol(k,1,n)+sol(k,j,n))
                
        if j>0:
            for k in range(1,j):
                max2=max(max2,sol(n,k,n)+sol(i,k,n))
        M[i][j]=max1+max2
    return M[i][j]
def main():
    global M
    case=0
    Matriz=0
    while True:
        case=[int(x) for x in sys.stdin.readline().strip().split()]
        if len(case)==0:
            break
        n=case[0]
        start=case[1]
        M[n][1]=start
        print(sol(1,n,n))
            
        
main()
