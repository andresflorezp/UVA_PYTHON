import sys
def busqueda(l,p,u):
    count=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j]=="@":
                l[i][j]="X"
                def recorrer(l,m,n):
                    nonlocal count
                    dx = [0,1,-1,0,1,1,-1,-1]
                    dy = [-1,0,0,1,-1,1,-1,1]
                    for z,k in zip(dx,dy):
                        for u in l:
                            if l[m][n]=="@":
                                l[m][n]="X"
                                
                                return  recorrer(l,m+z,n+k)
                        for u in l:
                            print(u)
                        print()
                        
                recorrer(l,i,j)
            
    return count
   
                
def main():
    val=0
    while True:
        val = [int(x) for x in sys.stdin.readline().strip().split()]
        if val == [0,0]:
            break
        lectura = []
        case = 0
        for i in range(val[0]):
            case = list(sys.stdin.readline().strip())
            lectura.append(case)
        print(busqueda(lectura,0,0))
main()

        
            
        
        
