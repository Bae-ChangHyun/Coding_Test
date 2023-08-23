import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    a,b=1,1
    w,e=map(int,input().split())
    for j in range(e,e-w,-1):
        a=a*j
    for j in range(w,0,-1):
        b=b*j
    print(a//b)