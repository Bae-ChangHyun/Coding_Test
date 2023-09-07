import sys
from collections import deque
input= sys.stdin.readline

def bfs(x,y):
        Q=deque()
        Q.append((x,y))
        visit[x][y]=1
        while Q:
            x,y=Q.popleft()
            for i in range(4):
                n_x,n_y=x+direct[i][0],y+direct[i][1]
                if(0<=n_x<n and 0<=n_y<n):
                    if(visit[n_x][n_y]==0 and graph[n_x][n_y]==graph[x][y]):
                        visit[n_x][n_y]=1
                        Q.append((n_x,n_y))  
        return 0

n=int(input())
direct=[[1,0],[-1,0],[0,1],[0,-1]]
graph = [list(input()) for _ in range(n)]
answer=[]

visit=[[0]*n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if(visit[i][j]==0):
            
            bfs(i,j)
            cnt+=1
answer.append(cnt)

visit=[[0]*n for _ in range(n)]
cnt=0

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'

for i in range(n):
    for j in range(n):
        if(visit[i][j]==0):
            bfs(i,j)
            cnt+=1
answer.append(cnt)

print(*answer)

