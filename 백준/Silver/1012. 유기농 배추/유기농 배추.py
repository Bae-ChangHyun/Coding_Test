import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(idx1, idx2):
    Q = deque()
    Q.append((idx1, idx2))
    visit[idx1][idx2] = 1
    
    while Q:
        idx1, idx2 = Q.popleft()
        
        for i in direct:
            n_idx1 = idx1 + i[0]
            n_idx2 = idx2 + i[1]
            
            if 0 <= n_idx1 < m and 0 <= n_idx2 < n:
                if visit[n_idx1][n_idx2] == 0 and graph[n_idx1][n_idx2] == 1:
                    Q.append((n_idx1, n_idx2))
                    visit[n_idx1][n_idx2] = 1

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visit = [[0] * n for _ in range(m)]
    cnt = 0
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    for i in range(m):
        for j in range(n):
            if visit[i][j] == 0 and graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)
