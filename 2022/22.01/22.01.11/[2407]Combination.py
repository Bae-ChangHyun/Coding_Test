import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dp=[]
for i in range(n+1):
    dp.append([0 for j in range(i+1)])
dp[1][0],dp[1][1]=1,1
for i in range(2,n+1):
    for j in range(0,i+1):
        if(j==0 or j==i):
            dp[i][j]=1
            continue
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
print(dp[n][m])