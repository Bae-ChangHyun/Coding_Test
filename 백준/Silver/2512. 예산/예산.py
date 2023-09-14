import sys
input= sys.stdin.readline
from bisect import bisect_left, bisect_right

N=int(input())
budget=list(map(int,input().split()))
target=int(input())
start,end=0,max(budget)

while(start<=end):
    
    mid=(start+end)//2
    tmp=sum([mid if i>=mid else i for i in budget])
    
    if(tmp>target):
        end = mid-1
    else:
        start = mid+1   
print(end)