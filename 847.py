import sys
while True:
    try:
        val=int(sys.stdin.readline().strip())
        count=0
        mul=1
        while True:
            if mul>=val:
                if count%2==0:
                    print("Ollie wins.")
                else:
                    print("Stan wins.")
                break

            mul*=9
            count+=1

        mul=1
        count=0
    except:
        break
