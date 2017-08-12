import sys
def orden(link,dates,maxi):
    guarda=list(zip(link,dates))
    almacen=[]
    for i in guarda:
        if i[1]==maxi:
            almacen.append(i[0])

    return almacen
    
def main():
    case = int(sys.stdin.readline().strip())
    count=case*10
    val=0
    links=[]
    valores=[]
    dates=1
    for i in range(case):
        for i in range(10):
            dato,val=sys.stdin.readline().strip().split()
            links.append(dato)
            valores.append(int(val))
        maximo=max(valores)
        guarda=list(orden(links,valores,maximo))
        print("Case #{}:".format(dates))
        for i in guarda:
            print(i)
        dates+=1
        del links
        links=[]
        del valores
        valores=[]
main()
        
            
        
        
