import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
dp=[1 for _ in range(n)]

for i in range(n):
    tmp=num[i]
    array=[0]
    for j in range(i):
        if(num[j]<tmp):
            array.append(dp[j])
    dp[i]=max(array)+1
#print(dp)
print(max(dp))