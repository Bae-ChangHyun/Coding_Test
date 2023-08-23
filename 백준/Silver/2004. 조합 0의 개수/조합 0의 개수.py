def counts(i, j):
    count = 0
    while i:
        i //= j
        count += i
    return count

import sys

a,b=map(int,sys.stdin.readline().split())
min5=counts(a,5)-counts(a-b,5)-counts(b,5)
min2=counts(a,2)-counts(a-b,2)-counts(b,2)
if(min(min5,min2)<0):
    print(0)
else:
    print(min(min5,min2))