import sys
from collections import deque
input= sys.stdin.readline

direct=[[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,-1],[-1,1]]

def bfs(x,y):
        Q=deque()
        Q.append((x,y))
        visit[x][y]=1
        
        while Q:
            x,y=Q.popleft()
            for i in range(8):
                n_x,n_y=x+direct[i][0],y+direct[i][1]
                if(0<=n_x<h and 0<=n_y<w):
                    if(visit[n_x][n_y]==0 and graph[n_x][n_y]==1):
                        visit[n_x][n_y]=1
                        Q.append((n_x,n_y))  
        return 0

while(1):
    w,h=map(int,input().split())
    if(w==0 and h==0):
        break
    graph=[list(map(int,input().split())) for _ in range(h)]
    visit=[[0]*w for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if(graph[i][j]==1 and visit[i][j]==0):
                    bfs(i,j)
                    cnt+=1
    print(cnt)