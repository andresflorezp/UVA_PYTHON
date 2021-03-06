# Python program for Bellman-Ford's single source 
# shortest path algorithm.
 
from collections import defaultdict
import sys
#Class to represent a graph
class Graph:
 
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])
         
    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))
    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm.  The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
 
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0
 
 
        # Step 2: Relax all edges |V| - 1 times. A simple shortest 
        # path from src to any other vertex can have at-most |V| - 1 
        # edges
        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        # Step 3: check for negative-weight cycles.  The above step 
        # guarantees shortest distances if graph doesn't contain 
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.
 
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        return True
        self.printArr(dist)
        # print all distance


def main():
    case=int(sys.stdin.readline().strip())
    for i in range(case):
        valores=[int(x) for x in sys.stdin.readline().strip().split()]
        g = Graph(valores[1])
        for i in range(valores[1]):
            val=[int(x) for x in sys.stdin.readline().strip().split()]
            g.addEdge(val[0],val[1],val[2])
        if g.BellmanFord(0):
            print("possible")
        else:
            print("not possible")
        del g
     
main()
