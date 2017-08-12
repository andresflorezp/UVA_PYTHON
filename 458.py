import sys
def change(L):
    cambio=[]
    for i in L:
        cambio.append(chr(ord(i)-7))
    return cambio

def main():
    val=sys.stdin.readline().strip()
    while val!="":
        val=list(val)
        print("".join(change(val)))
        val=sys.stdin.readline().strip()
        
main()        
