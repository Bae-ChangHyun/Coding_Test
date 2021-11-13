row,column=map(int,input().split())
tmp=list(map(int,input().split()))

res,index=0,0
start=tmp[0]

for i in range(len(tmp)-1):
    if(tmp[i+1]>=start or i+1==len(tmp)-1):
        start=min(start,tmp[i+1])
        res=res+start*(i-index)-sum(tmp[index+1:i+1])
        index=i+1
        start=tmp[i+1]
print(res)
        