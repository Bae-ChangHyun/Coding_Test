from sys import stdin

n = int(stdin.readline())
tmp=[i for i in range(1,10)]
dp= [[0] * 10 for _ in range(n + 1)]
dp[0]=[1,1,1,1,1,1,1,1,1,1]
for i in range(1,n+1):
    for j in range(0,10):
        if(j==0):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i][j-1]+dp[i-1][j]
#print(dp[n-1])
print(sum(dp[n-1])%10007)