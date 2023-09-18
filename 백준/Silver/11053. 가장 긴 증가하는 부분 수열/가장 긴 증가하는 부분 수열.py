import sys

input = sys.stdin.readline

n=int(input())
dp=[0]*n
dp[0]=1
array=list(map(int,input().split()))

for i in range(1,n):
    tmp=[dp[j] for j in range(i) if(array[j]<array[i])]
    if(tmp==[]):tmp.append(0)
    dp[i]=max(tmp)+1
print(max(dp))
    