import sys
input=sys.stdin.readline

r,c,w=map(int,input().split())
dp=[]
res=0
for i in range(r+w+1):
    dp.append([0]*(i+1))
    
for i in range(r+w+1):
    for j in range(i+1):
        if(j==0 or j==i):
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            
for i in range(r-1,r+w-1):
    for j in range(c-1,c-1+i-r+2):
        res+=dp[i][j]
print(res)