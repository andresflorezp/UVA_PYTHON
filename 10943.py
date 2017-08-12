#Permutaciones 

import sys
memo=None

def solve(n,k):
    global memo
    if k==1 or n==0:
        return 1
    elif memo[n][k]!=None:
        return memo[n][k]
    else:
        
        for i in range(n+1):
            memo[n][k]=0
            memo[n][k]=(solve(n,k-1)+solve(n-1,k))% 1000000

    return memo[n][k]
        
def main():
    global memo
    memo=[[None for i in range(101)] for i in range(101)]
    n,k=[int(x) for x in sys.stdin.readline().strip().split()]
    while (n+k>0):
        print(solve(n,k))
        n,k=[int(x) for x in sys.stdin.readline().strip().split()]
main()
