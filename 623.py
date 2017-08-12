from math import *
import sys
def sol():
    val=0
    while True:
        val=sys.stdin.readline().strip()
        if val=="":
            break
        print("{}!".format(val))
        print(factorial(int(val)))
sol()

