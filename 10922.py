import sys
def sol(val):
    count=0
    for i in val:
        count+=int(i)
    if count%9==0:
        
        return (True,len(str(count)))
    else:
        return (False,0)



def main():
    val=1
    while True:
        val=int(sys.stdin.readline().strip())
        if val==0:
            break
        pre=sol(str(val))
        if pre[0]:
            print("{} is a multiple of 9 and has 9-degree {}.".format(val,pre[1]))
        elif not pre[0]:
            print("{} is not a multiple of 9.".format(val))

main()            
    
    
    
