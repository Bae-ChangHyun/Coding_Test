"""
row,column=map(int,input().split())
tmp=list(map(int,input().split()))
res,index=0,0

start=tmp[0]
for i in range(len(tmp)-1):     
    if(tmp[i+1]>=start or (i+1==len(tmp)-1 and tmp[i+1]!=0)):  #기둥이 정해진지점보다 같아지거나 높아질 때 혹은 마지막이면서 마지막기둥이 0이 아닐 때
        res=res+start*(i-index)-sum(tmp[index+1:i+1]) # 그 사이 빗물을 계산한다.
        index=i+1 #새로운지점의 인덱스
        while(1):                        #가장 높은 기둥이 한개만 있으면 그 기둥은 의미없어서 한칸씩 줄임 가장 높은게 한개가 아닐때까지
            if(i+1==len(tmp)-1):
                break
            todel=max(tmp[i+1:])
            if(tmp[i+1:].count(todel)==1):
                didx=tmp[i+1:].index(todel)
                tmp[i+1+didx]-=1
            else:
                break
        start=tmp[i+1] #새로운 지점
print(res)
"""
h,w=map(int,input().split())
m=list(map(int,input().split()))
s=0
for i,d in enumerate(m):
    s+=min(max(m[:i+1]),max(m[i:]))-d
print(s)
        