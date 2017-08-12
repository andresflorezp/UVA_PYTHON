import sys
def cambioB(num):
    conta=[]
    while num!=1:
        conta.append(str(num%2))
        num=num//2
    conta.append("1")
    return(conta[::-1])


def main():
    case=[0]
    while len(case)!=0:
        try:
            case = [int(x) for x in sys.stdin.readline().strip().split()]
            temp=cambioB(case[0])
            temp2=cambioB(case[1])
            container=""
            dif=len(temp)-len(temp2)
            dif2=len(temp2)-len(temp)
            if dif ==0:
                pass
            elif dif>dif2:
                for i in range(dif):
                    temp2.insert(0,"0")
            elif dif2>dif:
                for i in range(dif2):
                    temp.insert(0,"0")
            for i,j in zip(temp[::-1],temp2[::-1]):
                if i==j:
                    container+="0"
                else:
                    container+="1"
            print(int(container,2))
        except:
            break

main()
        
        

        
    
