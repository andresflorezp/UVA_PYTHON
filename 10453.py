import sys
def sol():
    val=0
    while val!="":
        val=list(sys.stdin.readline().strip())
        count=0
        count2=1
        if val==val[::-1]:
            print("0 {}".format("".join(val)))
        else:
            val.append(val[0])
            while  val!=val[::-1]:
                val.insert(count2*-1,val[count2])
                count2+=1
                count+=1
            print(str(count2)+" "+"".join(val))
            count2=0
            count=0
sol()

        
