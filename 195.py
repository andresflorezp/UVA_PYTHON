from itertools import *
import sys
def main():
    case = int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val = sys.stdin.readline().strip()
        guarda = sorted(set(permutations(val)))
        for i in guarda:
            print("".join(i))


main()
    
