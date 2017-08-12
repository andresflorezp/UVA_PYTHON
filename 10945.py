import sys
def quitar(pal):
    pal=pal.replace(",","")
    pal=pal.replace("!","")
    pal=pal.replace(".","")
    pal=pal.replace("?","")
    pal=pal.replace(" ","")

    return pal

    
    
def main():
    val=0
    while True:
        val=sys.stdin.readline().strip()
        if val=="DONE":
            break
        val=val.lower()
        val=quitar(val)
        if val==val[::-1]:
            print("You won't be eaten!")
        else:
            print("Uh oh..")
main()
