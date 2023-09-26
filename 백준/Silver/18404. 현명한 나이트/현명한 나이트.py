from collections import deque
from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 판 크기, 상대편 수
x, y = map(int, input().split())  # 나이트 위치
visit = [[0]*(n+1) for i in range(n+1)]  # 방문 횟수 기록
target = []
dir = [[-2, -1], [-2, 1], [-1, -2], [-1, 2],
       [1, -2], [1, 2], [2, -1], [2, 1]]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in dir:
            nowx, nowy = x+i[0], y+i[1]
            if (1 <= nowx <= n and 1 <= nowy <= n and visit[nowx][nowy] == 0):
                q.append((nowx, nowy))
                visit[nowx][nowy] = visit[x][y]+1

for i in range(m):
    target.append(list(map(int, input().split())))
bfs(x, y)
for i in target:
    print(visit[i[0]][i[1]])
