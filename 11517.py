import sys
infinito = 10006
maximo=10005
def DP(total,valores):
    dp=[infinito for i in range(10005)]
    dp[0]=0
    for u in valores:
        for i in range(u,maximo):
            dp[i]=min(dp[i],dp[i-u]+1)
    pos=total
    extraer=dp[pos:]
    val=min(extraer)
    indice=extraer.index(val)
    print(extraer)
    while pos<maximo and dp[pos]==infinito:
        pos+=1
    return pos,dp[pos]
                


    
def main():
    case=int(sys.stdin.readline().strip())
    for i in range(case):
        valores=[]
        total=int(sys.stdin.readline().strip())
        dates=int(sys.stdin.readline().strip())
        for j in range(dates):
            valores.append(int(sys.stdin.readline().strip()))
        sol=DP(total,valores)
        print(sol[0],sol[1])
main()
