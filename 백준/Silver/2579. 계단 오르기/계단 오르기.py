# 2579번: 계단 오르기
import sys
input = sys.stdin.readline

N=int(input())
a=[0]*(N+1)
dp=[0]*(N+1)

for i in range(1,N+1):
    a[i]=int(input())

if N == 1:
    print(a[1])
    sys.exit(0)
if N == 2:
    print(a[1] + a[2])
    sys.exit(0)

dp[1]=a[1]
dp[2]=a[2]+a[1]

for i in range(3,N+1):
    dp[i]=max(a[i]+a[i-1]+dp[i-3],a[i]+dp[i-2])
print(dp[N])