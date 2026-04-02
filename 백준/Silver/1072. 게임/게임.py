import sys
input = sys.stdin.readline

x, y = map(int, input().split())
limit = (y * 100) // x          # 현재 승률 Z

# 99% 이상이면 절대 변하지 않음
if limit >= 99:
    print(-1)
    sys.exit()

def min_games(x, y, limit):
    start, end = 1, 1_000_000_000
    ans = -1

    while start <= end:
        mid = (start + end) // 2
        new_rate = ((y + mid) * 100) // (x + mid)

        if new_rate > limit:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

print(min_games(x, y, limit))