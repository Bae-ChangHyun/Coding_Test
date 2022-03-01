import sys

input=sys.stdin.readline
an,bn=map(int,input().split())

a=set(map(int,input().split()))
b=set(map(int,input().split()))

k=a&b

print(an+bn-len(k)*2)

