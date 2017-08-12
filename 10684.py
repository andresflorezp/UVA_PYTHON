import sys

def Kadane(V):
    sum_actual=0
    maxi=0
    container=[]
    for i in range(len(V)):
        sum_actual+=V[i]
        container.append(str(V[i]))
        if sum_actual<0:
            sum_actual=0
            del container
            container=[]
        if maxi<sum_actual:
            maxi=sum_actual

    return maxi

def main():
    case =1
    count=0
    container=[]
    val=0
    while True:
        case = sys.stdin.readline().strip()
        if case=="0":
            break
        if case != "":
            pass
        
            while count!=int(case):
                val= [int(x) for x in sys.stdin.readline().strip().split()]
                count+=len(val)
                for i in val:
                    container.append(i)
            guarda=Kadane(container)
            
            if guarda!=0:
                print("The maximum winning streak is {}.".format(guarda))
            elif guarda==0:
                print("Losing streak.")
            del container
            container=[]
            count=0
main()
        
    
