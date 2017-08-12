import sys    
def main():
    case=int(sys.stdin.readline().strip())
    value=0
    for i in range(case):
        val=int(sys.stdin.readline().strip())
        container={}
        maxi,count,start=0,0,0
        for i in range(val):
            value=int(sys.stdin.readline().strip())
            if value in container:
                pos=container[value]
                if pos>=start:
                    start=pos+1
                maxi=max(maxi,i-start+1)
                container[value]=i
            else:
                container[value]=i
                maxi=max(maxi,i+1-start)
        print(maxi)
        del container
        container={}
main()
            
        
