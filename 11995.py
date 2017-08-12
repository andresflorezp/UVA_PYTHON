import sys
from collections import deque
from heapq import *


while True:
    try:
        N = int(sys.stdin.readline().strip())
    except:
        break
    stack = []
    queue = deque()
    heap = []
    isStack = isQueue = isHeap = True
    for i in range(N):
        try:
            line = [int(x) for x in sys.stdin.readline().strip().split()]
            if line[0] == 1:
                stack.append(line[1])
                queue.append(line[1])
                heap.append(line[1])
                heap=sorted(heap)
            else:
                a = stack.pop()
                if a != line[1]:
                    isStack = False
                a = queue.popleft()
                if a != line[1]:
                    isQueue = False
                a = heap.pop()
                if a != line[1]:
                    isHeap = False
        except:
            isStack = isQueue = isHeap = False
            continue
    s = sum([isStack, isQueue, isHeap])
    if s >= 2:
        print ('not sure')
    elif s == 0:
        print ('impossible')
    else:
        if isStack:
            print ('stack')
        if isQueue:
            print ('queue')
        if isHeap:
            print ('priority queue')
