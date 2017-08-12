import sys
def sol(N,array):
    array.sort()
    d = 0
    if N % 2:
        mid = array[N // 2]
    else:
        mid = 0.5 * (array[N // 2 - 1] + array[N // 2])
    for a in array:
        d += abs(a - mid)
    return int(d)
    
def main():
    case = int(sys.stdin.readline().strip())
    val=0
    for i in range(case):
        val=[int(x) for x in sys.stdin.readline().strip().split()]
        print(sol(val[0],val[1:]))
main()
