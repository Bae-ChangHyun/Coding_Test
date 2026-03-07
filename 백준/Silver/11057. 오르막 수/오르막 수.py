# 11057번: 오르막 수
import sys
input = sys.stdin.readline

N=int(input())

dp=list([0]*10 for _ in range(N+1))

dp[0]=[1,1,1,1,1,1,1,1,1,1]

for i in range(1,N+1):
    for j in range(10):
        if j==0:dp[i][j]=1
        else:dp[i][j]=dp[i][j-1]+dp[i-1][j]
print(dp[N][9]%10007)
        