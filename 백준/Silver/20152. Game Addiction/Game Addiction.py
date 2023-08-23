import sys
input=sys.stdin.readline

h,n=map(int,input().split())
if(n>h):
    h,n=n,h
dp=[]

for i in range(h+1):
    dp.append([0]*(i+1))

for i in range(h,n-1,-1):
    for j in range(h,n-1,-1):
        if(i==h):
            dp[i][j]=1
        elif(j>i):
            continue
        else:
            if(i==j):
                dp[i][j]=dp[i+1][j]
            else:
                dp[i][j]=dp[i][j+1]+dp[i+1][j]
#print(dp)
print(dp[n][n])