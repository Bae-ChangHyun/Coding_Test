from collections import deque

N = int(input())
tech = deque(map(int, input().split()))
card = deque(range(1, N+1))
origin = deque()
while tech:
    t = tech.pop()
    a = card.popleft()
    if t == 1:
        origin.appendleft(a)
    elif t == 2:
        origin.insert(1, a)
    elif t == 3:
        origin.append(a)
print(*origin)