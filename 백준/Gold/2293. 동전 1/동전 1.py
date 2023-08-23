import sys
from itertools import combinations
input=sys.stdin.readline

n,k=map(int,input().split())
coin=[]
dp=[1]+[0 for i in range(k)]

for i in range(n):
    coin.append(int(input()))

for i in range(len(coin)):
    for j in range(0,k+1):
        if(j-coin[i]>=0):
            dp[j]+=dp[j-coin[i]]
print(dp[k]) 