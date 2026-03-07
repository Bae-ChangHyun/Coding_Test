# 2156번: 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
else:
    dp = [0] * (n + 1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    dp[3] = max(dp[2], wine[1] + wine[3], wine[2] + wine[3])

    for i in range(4, n + 1):
        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + wine[i],
            dp[i - 3] + wine[i - 1] + wine[i]
        )

    print(dp[n])