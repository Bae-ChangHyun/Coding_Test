import sys
from collections import deque

def bfs(idx):
    result = 0
    Q=deque()
    Q.append(idx)
    while Q:
        a=Q.popleft()
        direct[2]=a
        if(a==k):
            result+=1
            continue
        for i in range(3):
            new_a=a+direct[i]  
            if(0<=new_a<=limit*2 and (visit[new_a]==0 or visit[new_a]==visit[a]+1)):
                Q.append(new_a)
                visit[new_a]=visit[a]+1
    return result

input = sys.stdin.readline

n,k=map(int,input().split())
direct=[-1,1,0]

limit=max(n,k)
visit=[0 for i in range(2*limit+1)]

result=bfs(n)
print(visit[k])
print(result)
