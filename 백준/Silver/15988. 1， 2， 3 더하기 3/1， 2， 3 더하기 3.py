# 15988번: 1, 2, 3 더하기 3
import sys
input = sys.stdin.readline

T=int(input())
n=[]

for i in range(T):
    n.append(int(input()))

max_n=max(n)+1
dp=[0]*(max_n)

dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,max_n):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009
    
for i in n:
    print(dp[i],end="\n")    