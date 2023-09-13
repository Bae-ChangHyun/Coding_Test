import sys
input=sys.stdin.readline

k,n=map(int,input().split())
line=[int(input()) for _ in range(k)]

start,end=0,max(line)+1
while(start<end):
    
    mid=(start+end)//2
    tmp=sum([i//mid for i in line])
    
    if(tmp<n):
        end = mid
    else:
        start = mid + 1
        
print(end-1)       