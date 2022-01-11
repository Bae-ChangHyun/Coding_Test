import sys
input=sys.stdin.readline

n=int(input())
a,b=0,1

for i in range(n+1):
    a,b=(a+b)%1000000007,a
print(b)