import sys
input=sys.stdin.readline

n=int(input())
dp=[0 for i in range(n+1)]

for i in range(1,n+1):
    if(i>=7):
        dp[i]=min(dp[i-1],dp[i-2],dp[i-5],dp[i-7])+1
    elif(i>=5):
        dp[i]=min(dp[i-1],dp[i-2],dp[i-5])+1
    elif(i>=2):
        dp[i]=min(dp[i-1],dp[i-2])+1
    else:
        dp[i]=dp[i-1]+1
print(dp[n])
    
    