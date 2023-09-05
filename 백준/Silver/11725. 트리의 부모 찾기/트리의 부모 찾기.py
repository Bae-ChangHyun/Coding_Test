import sys
from collections import deque
input= sys.stdin.readline

def bfs(idx):
    Q=deque()
    Q.append(idx)
    visited[idx]=1
    
    while Q:
        a=Q.popleft()
        for i in graph[a]:
            if(visited[i]==0):
                parents[i]=a
                Q.append(i)
                visited[i]=1
    return 0

n=int(input())

graph=[[] for _ in range(n+1)]
visited=[0 for i in range(n+1)]
parents=[0 for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(*parents[2:])