import sys
def cambio(valores,sames):
    for i in range(len(sames)):
        if sames[i]!="X":
            guarda=int(sames[i])
            valores[i]=valores[guarda-1]

    return valores
            
    
def main():
    case = int(sys.stdin.readline().strip())
    conta=0
    almacen=[]
    same=[]
    p=0
    for i in range(case):
        conta = int(sys.stdin.readline().strip())
        val=0
        for j in range(conta):
            val=sys.stdin.readline().strip().split()
            if len(val)==1:
                almacen.append(val[0])
                same.append("X")
            elif len(val)==3:
                almacen.append(val[0])
                same.append(val[2])
        guarda=cambio(almacen,same)
        for i in guarda:
            if i=="LEFT":
                p-=1
            else:
                p+=1
        print(p)
        p=0
        del almacen
        almacen=[]
        del same
        same=[]
main()
        
                

        
                
            
            
        
    
