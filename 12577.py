import sys
def sol():
    val=0
    case=1
    while val!="*":
        val=sys.stdin.readline().strip()
        if val=="*":
            break
        elif val=="Hajj":
            print("Case {}: Hajj-e-Akbar".format(case))
        else:
            print("Case {}: Hajj-e-Asghar".format(case))

        case+=1

sol()
            
