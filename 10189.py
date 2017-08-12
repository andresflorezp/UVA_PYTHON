import sys
def cambio(M):
    for i in M:
        for j in range(len(i)):
            if i[j]==".": 
                i[j]=0
            

    return M

def recorrer(M,row,col):
    dx=[1,0,0,-1,1,-1,1,-1]
    dy=[0,-1,1,0,-1,-1,1,1]
    for i in range(row):
        for j in range(col):
            if M[i][j]=="*":
                for k,z in zip(dy,dx):
                    if 0<=i+k and i+k<row and 0<=j+z and j+z<col  and M[i+k][j+z]!="*":
                        M[i+k][j+z]+=1

    return M
            
    


def main():
    case=[1,1]
    count=1
    case=[int(x) for x in sys.stdin.readline().strip().split()]
    while case!=[0,0]:
        
        
        
        
        container=[]
        for i in range(case[0]):
            container.append(list(sys.stdin.readline().strip()))
        almacen=cambio(container)
        cambio2=recorrer(almacen,case[0],case[1])
        print("Field #{}:".format(count))
        
        for i in cambio2:
            print("".join(map(str,i)))
        count+=1
        case=[int(x) for x in sys.stdin.readline().strip().split()]
        if case==[0,0]:
            break
        if case!=[0,0]:
            print()
        

    

main()
