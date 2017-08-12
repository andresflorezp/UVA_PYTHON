import sys

def dfs(s):
    visited[s] = 1
    for i in reversed(range(m)):
        if not visited[i] and edges[s, i]:
            dfs(i)
    topoResult.append(s)


case = 0
while True:
    case += 1
    if case != 1:
        try:
            raw_input()
        except:
            break
    m = int(sys.stdin.readline().strip())
    names = {}
    nameId = []
    for i in range(m):
        nameId.append(sys.stdin.readline().strip())
        names[nameId[-1]] = i
    edges = np.zeros((m + 1, m + 1), dtype=np.int)
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        a, b = sys.stdin.readline().strip().split()
        edges[names[a], names[b]] = 1
    for i in range(m):
        edges[m, i] = 1
    topoResult = []
    visited = [0] * (m + 1)
    dfs(m)
    print ('Case #%d: Dilbert should drink beverages in this order:' % case,)
    for i in topoResult[:-1][::-1]:
        print (nameId[i]),
    print ('\n')
