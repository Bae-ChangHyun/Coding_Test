import sys
from collections import deque
input= sys.stdin.readline

n,m=map(int,input().split())

graph=[input().rstrip() for _ in range(n)]
visit=[[0]*(m) for _ in range(n)]
direct=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(x,y):
    Q=deque()
    Q.append((x,y))
    visit[x][y]=1

    while Q:
        x,y=Q.popleft()
        for i in range(4):
            n_x,n_y=x+direct[i][0],y+direct[i][1]
            if(0<=n_x<n and 0<=n_y<m):
                if(visit[n_x][n_y]==0 and graph[n_x][n_y]=='1'):
                    visit[n_x][n_y]=visit[x][y]+1
                    Q.append((n_x,n_y))  
    return 0

bfs(0,0)
#print(visit)
print(visit[n-1][m-1])