import sys
from collections import deque
input= sys.stdin.readline

n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]
visited=[0 for i in range(n+1)]

answer1,answer2=[],[]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,n+1):
    graph[i].sort()

def dfs(idx):
    visited[idx]=1
    answer1.append(idx)
    for i in graph[idx]:
        if(visited[i]==0):
            dfs(i)
    return 0

dfs(v)
print(*answer1)

visited=[0 for i in range(n+1)]

def bfs(idx):
    Q=deque()
    Q.append(idx)
    while Q:
        idx=Q.popleft()
        visited[idx]=1
        answer2.append(idx)
        for i in graph[idx]:
            if(visited[i]==0 and i not in Q):
                Q.append(i)
    return 0

bfs(v)
print(*answer2)