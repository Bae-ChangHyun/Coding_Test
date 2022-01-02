import sys

rankn,n = map(int, sys.stdin.readline().split())
all = [sys.stdin.readline().split() for _ in range(rankn)]
 
for i in range(n):
    tmp=int(sys.stdin.readline())
    left,right=0,rankn-1
    while(left<=right):
        mid=int((left+right)/2)
        if(tmp>int(all[mid][1])):
            left=mid+1
            mid=left
        else:
            right=mid-1
    print(all[mid][0])
