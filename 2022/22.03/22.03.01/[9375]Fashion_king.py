import sys

input=sys.stdin.readline

t=int(input())

for i in range(t):
    n=int(input())
    cloth=dict()
    tmp=1
    for j in range(n):
        a,b=input().split()
        if(b in cloth):
            cloth[b]+=1
        else:
            cloth[b]=1
    for k in cloth:
        tmp*=(cloth[k]+1)
    print(tmp-1)
