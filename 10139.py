import sys
from math import *
def main():
    case=[0]
    while len(case)!=0:
        try:
            case =[int(x) for x in sys.stdin.readline().strip().split()]
            val=factorial(case[0])
            if val%case[1]==0:
                print("{} divides {}!".format(case[1],case[0]))
            else:
                print("{} does not divide {}!".format(case[1],case[0]))
        except:
            break

main()
            
