import sys
def sol():
    val="0"
    count=1
    while val!= "#":
        val=sys.stdin.readline().strip()
        if val=="HELLO":
            print("Case {}: ENGLISH".format(count))
        if val=="HOLA":
            print("Case {}: SPANISH".format(count))
        if val=="HALLO":
            print("Case {}: GERMAN".format(count))
        if val=="BONJOUR":
            print("Case {}: FRENCH".format(count))
        if val=="CIAO":
            print("Case {}: ITALIAN".format(count))
        if val=="ZDRAVSTVUJTE":
            print("Case {}: RUSSIAN".format(count))
        if val!="HELLO" and val!="HOLA" and val!="HALLO" and val!="BONJOUR" and val!="CIAO" and val!="ZDRAVSTVUJTE" and val!="#":
            print("Case {}: UNKNOWN".format(count))
        count+=1
sol()
            












        
