import sys

input=sys.stdin.readline

n=int(input())

dp=[0,0,1,0,2,1]+[0 for _ in range(n+1)]

for i in range(6,n+1):
    if(dp[i-5]!=0 and dp[i-2]!=0):
        dp[i]=min(dp[i-2]+1,dp[i-5]+1)
    elif(dp[i-5]==0):
        dp[i]=dp[i-2]+1
    else:
        dp[i]=dp[i-5]+1
if(dp[n]==0):print(-1)
else:print(dp[n])