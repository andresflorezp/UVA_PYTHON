import sys
def N_R(input):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

def R_N(val):
    letras={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    val=list(val)
    suma=0
    re=0
    while re<len(val):
        if re+2<=len(val) and val[re]=="I" and val[re+1]=="V" :
            suma+=letras["V"]-letras["I"]
            re+=2
        elif re+2<=len(val) and val[re]=="I" and val[re+1]=="X":
            suma+=letras["X"]-letras["I"]
            re+=2
        elif re+2<=len(val) and val[re]=="X" and val[re+1]=="L":
            suma+=letras["L"]-letras["X"]
            re+=2
        elif re+2<=len(val) and val[re]=="X" and val[re+1]=="C":
            suma+=letras["C"]-letras["X"]
            re+=2
        elif re+2<=len(val) and val[re]=="C" and val[re+1]=="D":
            suma+=letras["D"]-letras["C"]
            re+=2
        elif re+2<=len(val) and val[re]=="C" and val[re+1]=="M":
            suma+=letras["M"]-letras["C"]
            re+=2
        elif val[re]=="V":
            suma+=letras["V"]
            re+=1
        elif val[re]=="L":
            suma+=letras["L"]
            re+=1
        elif val[re]=="D":
            suma+=letras["D"]
            re+=1
        elif val[re]=="I":
            suma+=letras["I"]
            re+=1
        elif val[re]=="X":
            suma+=letras["X"]
            re+=1
        elif val[re]=="C":
            suma+=letras["C"]
            re+=1
        elif val[re]=="M":
            suma+=letras["M"]
            re+=1
    return suma
            

    
def main():
    val=0
    numeros=[str(i) for i in range (10) ]
    letras=["I","V","X","L","C","D","M"]
    while True:
        val=sys.stdin.readline().strip()
        if val=="":
            break
        if val=="4000":
            print("MMMM")
        elif val=="MMMM":
            print(4000)
            
        elif val[0] in numeros:
            print(N_R(int(val)))
        elif val[0] in letras:
            print(R_N(val))
main()
        
            
    
