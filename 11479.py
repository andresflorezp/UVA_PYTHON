from itertools import *
import sys
def invalid(l):
    veri=True
    for i in l:
        if i[0]+i[1]<=i[2]:
            veri=False

    return veri

    
def main():
    case=int(sys.stdin.readline().strip())
    val=0
    count=1
    for i in range(case):
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        pre=sorted(permutations(val))
        guarda=invalid(pre)
        veri2=True
        if guarda and val[0]==val[1]==val[2]:
            print("Case {}: Equilateral".format(count))
        elif guarda:
            if(val[0]==val[1]) and veri2 :
                print("Case {}: Isosceles".format(count))
                veri2=False
            if(val[0]==val[2]) and veri2:
                print("Case {}: Isosceles".format(count))
                veri2=False
            if (val[1]==val[2])and veri2:
                print("Case {}: Isosceles".format(count))
                veri2=False
            if val[0]!=val[1] and val[0]!=val[2] and val[0]!=val[2] and veri2:
                print("Case {}: Scalene".format(count))
                veri2=False
                

    
        elif not guarda:
            print("Case {}: Invalid".format(count))
        count+=1
            

main()
            
            
        
        
