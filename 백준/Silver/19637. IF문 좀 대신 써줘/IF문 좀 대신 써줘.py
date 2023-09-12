import sys

def binary_search(li, n, start, end):
    if start > end:
        return li[start][0]
    
    mid = (start + end) // 2
    
    if int(li[mid][1]) >= n:
        return binary_search(li, n, start, mid - 1)
    else:
        return binary_search(li, n, mid + 1, end)

N, M = map(int, sys.stdin.readline().split())
li = [sys.stdin.readline().split() for _ in range(N)]
for _ in range(M):
    n = int(sys.stdin.readline())
    result = binary_search(li, n, 0, len(li) - 1)
    print(result)
