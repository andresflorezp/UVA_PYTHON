import sys
from math import *
def ecu(valores):
    concat="0."
    for  i in range(10):
        for  j in range(10):
            for  k in range(10):
                for  l in range(1,10):
                    concat=concat+str(i)+str(j)+str(k)+str(l)
                    concat=float(concat)
                    A=(valores[0]*e**(-1*concat))
                    B=(valores[1]*sin(concat))
                    C=(valores[2]*cos(concat))
                    D=(valores[3]*tan(concat))
                    E=((valores[4]*(concat)**2)+valores[5])
                    if A+B+C+D+E<=0.00005:
                        return(concat)
                    elif i==10 and A+B+C+D+E!=0:
                        return("No solution")
                    else:
                        concat="0."
                    
                        
def main():
    val=[0]
    while True:
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        if len(val)==0:
            break
        print(ecu(val))
main()
    
