def countss(n,a):
    cnt=0
    if(n<5):
        return 0
    if(n%a!=0):
        n=n//5*5
    while(1):
        if(n%5==0):
            cnt+=n//a
            n//=a
        else:
            break
    return cnt
def counts(i, j):
    count = 0
    while i:
        i //= j
        count += i
    return counts

import sys

a,b=map(int,sys.stdin.readline().split())
min5=counts(a,5)-counts(a-b,5)-counts(b,5)
min2=counts(a,2)-counts(a-b,2)-counts(b,2)
if(min(min5,min2)<0):
    print(0)
else:
    print(min(min5,min2))