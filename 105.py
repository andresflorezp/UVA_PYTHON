import sys
MAXN=1000
H = [0 for i in range(MAXN)]
while True:
    left, height, right = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(left, right + 1):
        H[i] = max(H[i], height)

        start = 0
    while H[start] == 0:
        start += 1
    print ('{} {}'.format(start, H[start]),"VAL"),
    for i in range(start + 1, MAXN):
        if H[i] != H[i - 1]:
            if H[i - 1] < H[i]:
                print ('{} {}'.format(i, H[i]),"VAL2"),
            else:
                print ('{} {}'.format(i - 1, H[i]),"VAL3")
