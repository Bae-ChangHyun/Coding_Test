import sys
from collections import deque

input = sys.stdin.readline

def mainS(t):
    global visit
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                if graph[i][j] in ['R','G'] and t == 1:
                    check=['R','G']
                else:check = [graph[i][j]]  
                bfs(i, j, check)
                cnt += 1
    return cnt

def bfs(x, y, check):
    Q = deque()
    Q.append((x, y))
    visit[x][y] = 1

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            n_x, n_y = x + direct[i][0], y + direct[i][1]
            if 0 <= n_x < n and 0 <= n_y < n:
                if visit[n_x][n_y] == 0 and graph[n_x][n_y] in check:
                    visit[n_x][n_y] = 1
                    Q.append((n_x, n_y))

n = int(input())
direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
graph = [input().rstrip() for _ in range(n)]
answer = []

for i in range(2):
    answer.append(mainS(i))

print(answer[0], answer[1])
