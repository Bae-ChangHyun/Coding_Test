import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
que=deque()
for i in range(n):
    m=list(input().split())
    if(m[0]=='push'):
        que.append(int(m[1]))
    elif(m[0]=='pop'):
        if(que):
            print(que.popleft())
        else:print(-1)
    elif(m[0]=='size'):
        print(len(que))
    elif(m[0]=='empty'):
        if(que):print(0)
        else:print(1)
    elif(m[0]=="front"):
        if(que):print(que[0])
        else:print(-1)
    else:
        if(que):print(que[-1])
        else:print(-1)
            
    