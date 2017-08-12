import sys
INF= 1<<30
while True:
    result = INF
    try:
        N,B,H,W =map(int,sys.stdin.readline().strip().split())
    except:
        break
    for i in range(H):
        P=int(sys.stdin.readline().strip())
        beds=map(int,sys.stdin.readline().strip().split())
        for b in beds:
            if b>=N and N *P <=B:
                result= min(result,N*P)

    if result!=INF:
        print(result)

    else:
        print("stay home")
    
