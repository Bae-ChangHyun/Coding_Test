"""
import sys

n,k=map(int,sys.stdin.readline().split())
idx,tmp=0,[]
que,que2=[i for i in range(n,0,-1)],[]

while(1):
    if(que==[]):
        if(que2==[]):
            break
        que,que2=que2,que
        que=list(reversed(que))
    if(idx!=k-1):
        que2.append(que[-1])
        que.pop()
        idx+=1
    elif(idx==k-1):
        tmp.append(que[-1])
        que.pop()
        idx=0
for i in range(len(tmp)):
    if(len(tmp)==1):
        print("<%i>"%tmp[i])
    elif(i==0):
        print("<%d"%tmp[i],end=",")
    elif(i==len(tmp)-1):
        print(" %d>"%tmp[i],end="")
    else:
        print(" %d"%tmp[i],end=",")
"""
n,m=map(int,input().split())
l=[*range(1,n+1)]
r=[]
i=0
while l:
    i=(i+m-1)%len(l)
    r+=[str(l.pop(i))]
print('<',', '.join(r), '>',sep='')
    