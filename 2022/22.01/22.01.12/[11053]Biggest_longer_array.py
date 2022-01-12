n=int(input())
A=list(map(int,input().split()))
DP=[0]*(max(A)+1)
for i in range(n):
    DP[A[i]]=max(DP[:A[i]])+1
print(DP)
print(max(DP))
"""
import sys
input=sys.stdin.readline

n,s=map(int,input().split())
num=list(map(int,input().split()))
dp=[0 for _ in range(n)]
answer=0

for i in range(len(num)):
    if(num[i]>=s):
        answer=i+1

for i in range(n):
    for j in range(n-i):
        dp[j]=dp[j]+num[j+i]
        if(dp[j]>=s):
            answer=i+1
            break
    if(answer!=0):
        break
    for j in range(n-i,n,1):
        dp[j]=0  
print(answer)
"""