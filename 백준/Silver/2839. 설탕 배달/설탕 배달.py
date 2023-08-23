import sys
input=sys.stdin.readline

n=int(input())
dp=[-1 for i in range(n+1)]

for i in range(n+1):
    # 3,5는 1로 고정 
    if(i==3 or i==5):
        dp[i]=1
        continue
    else:
        if(i>=5):
            if(dp[i-3]+1!=0):a=dp[i-3]+1
            else:a=99999
            if(dp[i-5]+1!=0):b=dp[i-5]+1
            else:b=99999
            dp[i]=min(a,b)
            if(dp[i]==99999):
                dp[i]=-1
print(dp[n])
