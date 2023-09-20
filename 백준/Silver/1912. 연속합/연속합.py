import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
dp=[0]*n

for i in range(n):
    if(num[i]>=0):dp[i]=max(0,dp[i-1])+num[i]
    else:  
        if(dp[i-1]+num[i]>=0):
            dp[i]=dp[i-1]+num[i]
        else:
            dp[i]=num[i] 
print(max(dp))