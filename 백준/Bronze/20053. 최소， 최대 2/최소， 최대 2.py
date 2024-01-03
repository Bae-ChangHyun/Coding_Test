import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    N=int(input())
    num=list(map(int,input().split()))
    num.sort()
    print(num[0],num[-1])