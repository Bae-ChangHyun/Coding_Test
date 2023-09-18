import sys
input = sys.stdin.readline

n=int(input())

dp=[-1]*(n+1)
sugar=[3, 5]

for i in range(3,n+1):
    if(i==3 or i==5):dp[i]=1
    for j in sugar:
        if(dp[i-j]!=-1):
            if(dp[i]==-1):dp[i]=dp[i-j]+1
            else:dp[i]=min(dp[i-j]+1,dp[i])
print(dp[n])