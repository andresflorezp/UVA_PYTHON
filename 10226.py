import sys
def main():
    case = int(sys.stdin.readline().strip())
    unicos = {}
    val = 0
    count=0
    cantidad=0
    blank=sys.stdin.readline().strip()
    while count!=case:
        val=sys.stdin.readline().strip()
        if val=="":
            count+=1
            
            for i in sorted(unicos):
                print(i,"{:0.4f}".format(unicos[i]*100/(cantidad)))
            cantidad=0
            del unicos
            unicos={}
            if count!=case:
                print()
                
        else:
            claves = unicos.keys()
            if val in claves:
                unicos[val]+=1
                cantidad+=1
            else:
                unicos[val]=1
                cantidad+=1          
        
        
main()
        
        
