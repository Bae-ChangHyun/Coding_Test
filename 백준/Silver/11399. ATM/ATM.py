import sys
input = sys.stdin.readline

n=int(input())
time=list(map(int,input().split()))

time.sort()

answer=[sum(time[:i]) for i in range(1,n+1)]

print(sum(answer))