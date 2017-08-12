import sys
def sol():
    case=int(sys.stdin.readline().strip())
    tam=0
    tamr=0
    conta=0
    for i in range(case):
        tam=list(map(int,sys.stdin.readline().strip().split()))
        campo=[[0 for i in range(tam[1]-2)]for j in range(tam[0]-2)]
        print(campo)
sol()
