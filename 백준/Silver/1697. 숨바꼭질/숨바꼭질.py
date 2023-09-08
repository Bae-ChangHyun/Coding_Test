import sys
from collections import deque

def bfs(idx):
    Q=deque()
    Q.append(idx)

    while Q:
        a=Q.popleft()
        direct[2]=a
        if(a==k):
            return visit[a]-1
        for i in range(3):
            new_a=a+direct[i]
            
            if(new_a<=limit*2):
                if(new_a>=0 and visit[new_a]==0):
                    Q.append(new_a)
                    visit[new_a]=visit[a]+1            

input = sys.stdin.readline

n,k=map(int,input().split())
direct=[-1,1,0]

limit=max(n,k)
graph=[i for i in range(2*limit+1)]
visit=[0 for i in range(2*limit+1)]

visit[n]=1
print(bfs(n))