import sys
def creciente(array):
    memo = [0]
    longest = [0] * (len(array)+1)
    longest[0] = 1
    for i in range(1, len(array)):
        if array[memo[-1]] < array[i]:
            memo.append(i)
            longest[i] = len(memo)
            continue
        low = 0
        high = len(memo) - 1
        while low < high:
            mid = (low + high) // 2
            if array[memo[mid]] < array[i]:
                low = mid + 1
            else:
                high = mid
        if array[i] < array[memo[low]]:
            memo[low] = i
        longest[i] = len(memo)

    return longest
            
        



def decreciente(array):

    memo = [0]
    longest = [0] * (len(array)+1)
    longest[0] = 1
    for i in range(1, len(array)):
        if array[memo[-1]] > array[i]:
            memo.append(i)
            longest[i] = len(memo)
            continue
        low = 0
        high = len(memo) - 1
        while low < high:
            mid = (low + high) // 2
            if array[memo[mid]] > array[i]:
                low = mid + 1
            else:
                high = mid
        # update if the new value is bigger
        if array[i] > array[memo[low]]:
            memo[low] = i
        longest[i] = len(memo)

    return longest
def sol(l):
    D=decreciente(l)
    C=creciente(l)
    ans=0
    for i in range(len(l)):
        ans = max(ans,C[i]+D[i]-1)
    return ans-1
        
    
    
def main():
    case = int(sys.stdin.readline().strip())
    container=[]
    t=0
    for i in range(case):
        val=int(sys.stdin.readline().strip())
        for i in range(val):
            t=int(sys.stdin.readline().strip())
            container.append(t)
        print(sol(container))
        del container
        container=[]
main()
            
    
