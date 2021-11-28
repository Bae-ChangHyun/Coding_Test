import sys
n=int(sys.stdin.readline())
check=[]

for i in range(n):
    tmp=sys.stdin.readline().rstrip()
    tmp=[i for i in tmp]
    for i in tmp:
        if(check=[]):
            check