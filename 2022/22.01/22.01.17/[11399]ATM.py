import sys
input=sys.stdin.readline

n,total=int(input()),0
p=list(map(int,input().split()))
p.sort()

for i in range(len(p)):
    total+=sum(p[:i+1])
print(total)