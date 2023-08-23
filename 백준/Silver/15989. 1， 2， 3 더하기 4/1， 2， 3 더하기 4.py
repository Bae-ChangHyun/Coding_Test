import sys
input=sys.stdin.readline

num,test=[1,2,3],[]
t=int(input())

for i in range(t):
    test.append(int(input()))

dp=[0 for i in range(max(test)+1)]
dp[0]=1

for i in range(len(num)):
    for j in range(0,max(test)+1):
        if(j-num[i]>=0):
            dp[j]+=dp[j-num[i]]
for i in test:
    if(i==0):print(0)
    else:print(dp[i])