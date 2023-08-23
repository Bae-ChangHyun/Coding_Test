import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a,b=1,1

if(n-m>m):m=n-m
for i in range(m):
    a*=n
    n-=1
    
for i in range(m):
    b*=m
    m-=1
print(a//b)