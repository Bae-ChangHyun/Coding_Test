import sys
input=sys.stdin.readline

k,n=map(int,input().split())
line=[int(input()) for _ in range(k)]

start,end=1,max(line)
while(start<=end):
    
    mid=(start+end)//2
    tmp=sum([i//mid for i in line])
    
    if(tmp<n):
        end = mid - 1
    else:
        start = mid + 1
        
print(end)       