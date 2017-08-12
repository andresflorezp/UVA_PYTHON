import sys
def contar(l):
    l=l.replace(".","")
    l=l.replace(",","")
    l=l.replace("¿","")
    l=l.replace("?","")
    l=l.replace("!","")
    l=l.replace("¡","")
    l=l.replace("*","")
    l=l.replace("(","")
    l=l.replace(")","")
    l=l.replace("[","")
    l=l.replace("]","")
    l=l.replace(";","")
    l=l.replace("-","")
    l=l.replace("+","")
    l=l.replace("´","")
    l=l.replace("'","")
    l=l.replace("*","")
    l=l.replace("/","")
    l=l.replace("-","")

    
    
    return(l)

def main():
    val = 0
    while True:
        val=sys.stdin.readline().strip()
        if val=="":
            break
        guarda=contar(val)
        
        guarda=guarda.split()
        print(len(guarda))
main()
        
