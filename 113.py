import sys
def main():
    a=0
    b=0
    while True:
        a=sys.stdin.readline().strip()
        if a=="":
            break
        b=sys.stdin.readline().strip()
        print(round(int(b)**(1/int(a))))
main()
