import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for i in range(t):
    order=1
    n,m=map(int,input().split())
    num=deque([i for i in range(0,n)])
    h=deque(list(map(int,input().split())))
    k=num[m]
    while(len(h)!=0):
        a=h[0]
        if(a!=max(h)):
            tmp=h.popleft()
            tmp2=num.popleft()
            h.append(tmp)
            num.append(tmp2)
        else:
            tmp=h.popleft()
            tmp2=num.popleft()
            if(tmp2==k):
                print(order)
                break
            order+=1