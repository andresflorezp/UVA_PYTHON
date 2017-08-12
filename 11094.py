import sys
def floodfill(L,x,y,V,N):
    dx=[1, 0,-1,0]
    dy=[0, 1,0,-1]
    if x<0 or x>=len(L) or y<0 or y>=len(L[0]):
        return 0
    if L[x][y]!=V:
        return 0
    suma=1
    L[x][y]=N
    for i in range(4):
        suma+=floodfill(L,x+dx[i],y+dy[i],V,N)
    return suma
            
        

def main():
    case=""
    container=[]
    contar=1
    count=0
    blank=0
    while True:
        case=[int(x) for x in sys.stdin.readline().strip().split()]
        if len(case)==0:
            case=[int(x) for x in sys.stdin.readline().strip().split()]
            if len(case)==0:
                break
            else:
                for i in range(int(case[0])):
                    container.append(list(sys.stdin.readline().strip()))
                datos=[int(x) for x in sys.stdin.readline().strip().split()]
                V=container[datos[0]][datos[1]]
                container[datos[0]][datos[1]]="^"
                for i in range(int(case[0])):
                    for j in range(int(case[1])):
                        if container[i][j]==V:
                            floodfill(container,i,j,V,"^")
                            count+=1
            print(count)
            contar+=1
            del container
            container=[]
            count=0
           
        for i in range(int(case[0])):
            container.append(list(sys.stdin.readline().strip()))
        datos=[int(x) for x in sys.stdin.readline().strip().split()]
        V=container[datos[0]][datos[1]]
        container[datos[0]][datos[1]]="^"
        for i in range(int(case[0])):
            for j in range(int(case[1])):
                if container[i][j]==V:
                    floodfill(container,i,j,V,"^")
                    count+=1
        print(count)
        contar+=1
        count=0
        del container
        container=[]
        
        
main()
