import sys
from collections import deque
input= sys.stdin.readline

n=int(input())

graph=[input().rstrip() for _ in range(n)]
visit=[[0]*(n) for _ in range(n)]
direct=[[0,1],[0,-1],[1,0],[-1,0]]
answer=[]

def bfs(x,y):
    Q=deque()
    Q.append((x,y))
    visit[x][y]=1
    cnt=1
    
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            n_x,n_y=x+direct[i][0],y+direct[i][1]
            if(0<=n_x<n and 0<=n_y<n):
                if(visit[n_x][n_y]==0 and graph[n_x][n_y]=='1'):
                    visit[n_x][n_y]=visit[x][y]+1
                    cnt+=1
                    Q.append((n_x,n_y))  
    return cnt

for i in range(n):
    for j in range(n):
        if(visit[i][j]==0 and graph[i][j]=='1'):
            answer.append(bfs(i,j))

print(len(answer))
answer.sort()
for i in range(len(answer)):print(answer[i])