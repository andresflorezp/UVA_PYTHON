#from math import *
import sys

def veri(val):
    count=0
    valor=str(val**2)
    
    for i in valor:
        count+=int(i)


    if count==1 or count==3 or count==4 or count==7 or count==9:
        return True
    else:
        return False


def main():
    val=1
    while True:
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        i=0
        while True:
            i+=1
            if veri(i) and (i+1)**2>val:
                print(i)
                break
            elif veri(i) and (i)**2==val:
                print(i)
                break

main()

            
        
    
