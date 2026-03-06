# 11055번: 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))

dp=[0]*N

dp[0] = a[0]

for i in range(1,N):
    dp[i] = a[i]
    for j in range(i):
        if a[j]<a[i]:
            dp[i] = max(dp[i],dp[j]+a[i])
print(max(dp))