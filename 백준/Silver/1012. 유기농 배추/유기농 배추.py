import sys
sys.setrecursionlimit(2_501)
from collections import deque
input= sys.stdin.readline

t=int(input())
direct=[[-1,0],[1,0],[0,-1],[0,1]]

def dfs(idx1,idx2):
    visit[idx1][idx2]=1
    for i in direct:
        n_idx1=idx1+i[0]
        n_idx2=idx2+i[1]
        if(n_idx1>=0 and n_idx1<m and n_idx2>=0 and n_idx2<n):
            if(visit[n_idx1][n_idx2]==0 and graph[n_idx1][n_idx2]==1):
                dfs(n_idx1,n_idx2)
                
    #print("here", idx1,idx2)
    return 0

for i in range(t):
    
    m,n,k=map(int,input().split())
    graph=[[0 for i in range(n)] for j in range(m)]
    visit=[[0 for i in range(n)] for j in range(m)]
    cnt=0
    
    for j in range(k):
        a,b=map(int,input().split())
        graph[a][b]=1  
          
    for j in range(m):
        for k in range(n):
            if(visit[j][k]==0 and graph[j][k]==1):
                dfs(j,k)
                cnt+=1  
    print(cnt)      
    #print(graph)