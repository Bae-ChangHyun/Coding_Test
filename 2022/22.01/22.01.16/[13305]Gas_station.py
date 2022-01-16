import sys
input=sys.stdin.readline

n=int(input())
k=list(map(int,input().split()))
cost=list(map(int,input().split()))
result=0

start=cost[0]
starti=0

for i in range(1,len(cost)):
    if(cost[i]<=start):
        result+=start*sum(k[starti:i])
        start=cost[i]
        starti=i
    else:
        if(i==len(cost)-1):
            result+=start*sum(k[starti:i+1])
print(result)
    