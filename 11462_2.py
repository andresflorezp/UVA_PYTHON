import sys
def merge(l):
    if len(l)>1:
        mid=len(l)//2
        partei=l[:mid]
        parted=l[mid:]
        merge(partei)
        merge(parted)
        i,j,k=0,0,0

        while i<len(partei) and j<len(parted):
            if partei[i]<parted[j]:
                l[k]=partei[i]
                i+=1
            elif parted[j]<partei[i]:
                l[k]=parted[j]
                j+=1
            k+=1

        while i<len(partei):
            l[k]=partei[i]
            i+=1
            k+=1
        while j<len(parted):
            l[k]=parted[j]
            j+=1
            k+=1
    return(l)
    i,j,k=0,0,0


def main():
    T=int(sys.stdin.readline().strip())
    val=list(map(int,sys.stdin.readline().strip().split()))
    while T!=0:
        print(merge(val))
        T=int(sys.stdin.readline().strip())
        val=list(map(int,sys.stdin.readline().strip().split()))
        

main()
    
        
