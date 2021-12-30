import sys
input=sys.stdin.readline

n=int(input())
tmp,dp=[],[]
for i in range(n):
    tmp.append(list(map(int,input().split())))
    dp.append([0]*n)
dp[0][0]=1

if(tmp[0][0]==0):
    print(0)
else:
    for i in range(n):
        for j in range(n):
            if(i==n-1 and j==n-1):
                break
            if(dp[i][j]==0):
                continue
            val=tmp[i][j]
            if(i+val<n):
                if(dp[i][j]!=0):
                    dp[i+val][j]+=dp[i][j]
                else:
                    dp[i+val][j]+=1
            if(j+val<n):
                if(dp[i][j]!=0):
                    dp[i][j+val]+=dp[i][j]
                else:
                    dp[i][j+val]+=1
    
    print(dp[n-1][n-1])