import sys
input=sys.stdin.readline

n,m=map(int,input().split())
tree=list(map(int,input().split()))

def binary_search(start,end):
    
    if(start>end):
        return end
    
    mid=(start+end)//2
    
    tmp=[i-mid for i in tree if i>mid]
    tmp=sum(tmp)
    #print(start, end ,mid, tmp)
    
    if(tmp==m):
        return mid
    elif(tmp<m):
        return binary_search(start,mid-1)
    else:
        return binary_search(mid+1,end)

print(binary_search(0,max(tree)))