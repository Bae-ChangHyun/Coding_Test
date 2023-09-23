import heapq
import sys
input = sys.stdin.readline
INF = int(1E9)

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
distance = [INF for _ in range(N+1)]
answer = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def dijkatra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for i in graph[now]:
            cost = distance[now]+1
            if (cost < distance[i]):
                distance[i] = cost
                heapq.heappush(q, (cost, i))


dijkatra(X)

for i in range(1, N+1):
    if (distance[i] == K):
        print(i)
        answer += 1
if (answer == 0):print(-1)
