import sys
input=sys.stdin.readline

n,m=map(int,input().split())
k=[int(input()) for _ in range(n)]

start,end=min(k), max(k)*m

while(start<=end):
    
    mid=(start+end)//2
    
    tmp=sum([mid//i for i in k])
    
    if(tmp>=m):
        end = mid-1
    else:
        start = mid+1
        
print(start)