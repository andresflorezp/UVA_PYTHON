import sys
class Nodo:
    def __init__(self,v,w):
        self.v = v
        self.w = w
    def __repr__(self):
        return "({},{})".format(self.v,self.w)
def bellmanFord(G,s):
    n = len(G)
    dist=[float("inf")]*n
    dist[s]=0
    for k in range(n):
        flag = False
        for u in range(n):
            for v in range(len(G[u])):
                if dist[G[u][v].v]>dist[u]+G[u][v].w:
                    dist[G[u][v].v]=dist[u]+G[u][v].w
                    flag=True
        
        if(not flag):break
   
    for u in range(n):
            for v in range(len(G[u])):
                if dist[G[u][v].v]>dist[u]+G[u][v].w:
                    return True
    return False
                    
    
    
                    
    
def main():
    casos = int(sys.stdin.readline().strip())
    for i in range(casos):
        g = [int(x) for x in sys.stdin.readline().strip().split()]
        V  = g[0]
        E  = g[1]
        G=[]
        for k in range(V):
            G.append([])
            
        for j in range(E):
            line = [int(x) for x in sys.stdin.readline().strip().split()]
            G[line[0]].append(Nodo(line[1],line[2]))
        if bellmanFord(G,0):print("possible")
        else:print("not possible")
            
main()
        
            
