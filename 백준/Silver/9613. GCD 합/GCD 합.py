import sys
import itertools

n=int(input())
sums=0

for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    for j in itertools.combinations(tmp[1:], 2):
        a,b=max(j[0],j[1]),min(j[0],j[1])
        while(b!=0):
            a=a%b
            a,b=b,a
        sums=sums+a
    print(sums)
    sums=0