import sys
def main():
    blank=0
    container=[]
    while True:
        try:
            queue = [int(x) for x in sys.stdin.readline().strip().split()]
            
            if not queue:
                blank+=1
            if blank>=2:
                for i in range(len(container)-1):
                    print(container[i])
                break
            if queue:
                blank=0
            
        except EOFError:
            break
        stack = []
        flag = True
        for q in queue:
            if q < 0:
                if not stack:
                    stack.append([q, abs(q)])
                    continue
                if stack and stack[-1][1] > abs(q):
                    stack[-1][1] -= abs(q)
                    stack.append([q, abs(q)])
                else:
                    flag = False
                    break
            else:
                if not stack or stack[-1][0] != -1 * q:
                    flag = False
                    break
                else:
                    stack.pop()
        if not flag or len(stack) > 0:
            container.append(':-( Try again.')
        else:
            container.append(':-) Matrioshka!')
        
            
                
main()

   
        
                


