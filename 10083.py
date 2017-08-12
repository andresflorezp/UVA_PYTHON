import sys


def veri(t,a,b):
    if len(str(((t**a)-1/(t**b)-1)))>100 or abs(int(((t**a)-1/(t**b)-1))-((t**a)-1/(t**b)-1))>0:
        return False
    else:
        return True
    
    




def main():
    val=[0]
    while True:
        try:
            val=[int(x) for x in sys.stdin.readline().strip().split()]
            if len(val)==0:
                break

            if veri(val[0],val[1],val[2]):
                print("({}^{}-1)/({}^{}-1) {}".format(val[0],val[1],val[0],val[2],int(((val[0]**val[1])-1)/((val[0]**val[2])-1))))
            elif not veri(val[0],val[1],val[2]):
                print("({}^{}-1)/({}^{}-1) is not an integer with less than 100 digits.".format(val[0],val[1],val[0],val[2]))
        except:
            print("({}^{}-1)/({}^{}-1) is not an integer with less than 100 digits.".format(val[0],val[1],val[0],val[2]))
            
main()
            
