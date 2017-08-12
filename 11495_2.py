import sys

num,lenn = None,None

def solve (num,low,hi):
    cont=0
    if low+1<hi:
        mid=low+((hi-low)//2)
        cont= solve(num,low,mid)
        cont+=solve(num,mid,hi)
        cont+=(merge(num,low,hi,mid))
    return cont

def merge(num,low,hi,mid):
    cont=0
    i,j=0,0
    pparte,sparte=num[low:mid],num[mid:hi] 
    for k in range(low,hi):
        if i==mid-low:
            num[k]=sparte[j]
            j+=1
        elif j==hi-mid:
            num[k]=pparte[i]
            i+=1
        else:
            if pparte[i]<sparte[j]:
                num[k]=pparte[i]
                i+=1
            else:
                num[k]=sparte[j]
                j+=1
                cont+=((mid-low)-i)
    return cont


def main():
  global num,lenn
  num=[1]
  while num[0]!=0:
    num = list(map(int,sys.stdin.readline().strip().split()))
    long=len(num)
    
    if num[0]==0:
        break
    res=solve(num,0,long)
    if res%2==0:
        print("Carlos")
    else:
        print("Marcelo")

        
  

main()

