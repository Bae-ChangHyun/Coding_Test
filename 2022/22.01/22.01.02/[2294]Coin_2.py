import sys
from itertools import combinations
input=sys.stdin.readline

n,k=map(int,input().split())
coin=[]
dp=[0 for i in range(k+1)]
tmp=[]

for i in range(n):
    coin.append(int(input()))
for j in range(1,k+1):
    for l in coin:
        if(j-l>=0):
            tmp.append(dp[j-l])
    if(tmp==[]):
        dp[j]=1
    else:
        dp[j]=min(tmp)+1
        tmp=[]
print(dp[k]) 
