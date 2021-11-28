import sys
n,k=map(int,sys.stdin.readline().split())

tmp=sorted(list(map(int,sys.stdin.readline().split())))
print(tmp[k-1])