import sys
a=[chr(i) for i in range(97,123)]
A=[chr(i) for i in range(65,91)]
abc=a+A
def es_primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
            # es divisible
            return False
    return True
 

    
def pala():
    val=0
    count=0
    while True:
        try:
            val=sys.stdin.readline().strip()
            if val=="":
                break
            for i in val:
                count+=abc.index(i)+1
            if es_primo(count):
                print("It is a prime word.")
            else:
                print("It is not a prime word.")

            count=0
        except:
            break
pala()
                
            
    
