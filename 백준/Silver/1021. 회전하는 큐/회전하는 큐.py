import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())

a=deque([i+1 for i in range(n)])
b=list(map(int,input().split()))
cnt=0
while(len(b)!=0):
    if(a[0]==b[0]):
        a.popleft()
        b.pop(0)
    else:
        ind=a.index(b[0])
        if(ind>len(a)/2):
            tmp=a.pop()
            a.appendleft(tmp)
        else:
            tmp=a.popleft()
            a.append(tmp)
        cnt+=1
print(cnt)
        