import sys
def Kadane(V):
    sum_actual=0
    maxi=0
    for i in V:
        sum_actual+=i
        if sum_actual<0:
            sum_actual=0
        if maxi<sum_actual:
            maxi=sum_actual

    return maxi



def main():
    val=[0]
    while len(val)!=0:
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        if len(val)==0:
            break
        print(Kadane(val))

main()
        
    
    
