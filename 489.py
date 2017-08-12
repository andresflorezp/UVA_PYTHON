import sys
def contar(word,letter):
    con=0
    for i in letter:
        busca=word.count(i)
        word=word.replace(i,"")
        
        if busca==0:
            con+=1
        if word=="":
            return "You win."
            break
        if word!="" and con>=7:
            return "You lose."
            break
    if word!="" and con<7:
        return "You chickened out."
    
        
def main():
    val=0
    palabra=0
    letras=0
    conta=1
    while True:
        val = int(sys.stdin.readline().strip())
        if val == -1:
            break
        palabra = sys.stdin.readline().strip()
        letras = sorted((sys.stdin.readline().strip()))
        guarda=contar(palabra,letras)
        print("Round {}".format(conta))
        print(guarda)
        conta+=1
main()
        
        
