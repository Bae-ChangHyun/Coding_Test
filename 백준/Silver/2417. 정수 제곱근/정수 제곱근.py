import sys
from collections import deque
from bisect import bisect_left,bisect_right
input=sys.stdin.readline

n = int(input())
def binary_search(target,start,end):
    
    mid=(start+end)//2
    if(start>end):
        return mid+1
    tmp=mid*mid
    if(tmp==target):
        return mid
    elif(tmp<target):
        return binary_search(target,mid+1,end)
    elif(tmp>target):
        return binary_search(target,start,mid-1)

print(binary_search(n,0,n))    