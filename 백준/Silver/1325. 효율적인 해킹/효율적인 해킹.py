from collections import deque
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

# bfs
ans = []
for i in range(1, N+1):
    visited = [False]*(N+1)
    queue = deque([i])
    visited[i] = True
    
    cnt = 1
    while queue:
        x = queue.popleft()
        for j in graph[x]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)
                cnt += 1
    ans.append(cnt)

max_cnt = max(ans)
for i in range(N):
    if ans[i] == max_cnt:
        print(i+1, end=" ")