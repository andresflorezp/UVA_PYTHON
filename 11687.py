import sys
while True:
    s = sys.stdin.readline().strip()
    if s == 'END':
        break
    elif s == "1":
        print (1)
        continue
    s = int(s)
    i = 1
    while True:
        d = len(str(s))
        if d == s:
            break
        else:
            s = d
            i += 1
    print (i)
print()
