import sys
def floodfill(L,x,y,V,N):
    dx=[1, 1, 0, -1, -1, -1,  0,  1]
    dy=[0, 1, 1,  1,  0, -1, -1, -1]
    if L[x][y]!=" ":
        return 
    
    L[x][y]="#"
    for i in range(8):
        if x+dx[i]>=0 and x+dx[i]<len(L) and y+dy[i]>=0 and y+dy[i]<len(L):
            return floodfill(L,x+dx[i],y+dy[i]," ","#")
    return L

    
    
def main():
    container=[]
    val=0
    while True:
        val=list(sys.stdin.readline().strip())
        if len(val)==0:
            break
        container.append(val)
    for i in container:
        print(i)
    for i in range(len(container)-1):
        for j in range(len(container[0])-1):
            if container[i][j]=="#":
                floodfill(container,i,j," ","#")
    for i in container:
        print("".join(i))
main()
                
                
            
