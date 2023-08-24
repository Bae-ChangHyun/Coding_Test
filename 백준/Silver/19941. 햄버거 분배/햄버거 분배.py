import sys
input=sys.stdin.readline

n,k=map(int,input().split())
answer=0
seat=input()
for i in range(len(seat)):
    if(seat[i]=='P'):
        start=max(0,i-k)
        end=min(n,i+k+1)
        temp=seat[start:end]
        idx=temp.find('H')
        if(idx==-1):continue
        temp=temp[:idx]+'X'+temp[idx+1:]
        seat=seat[:start]+temp+seat[end:]
        answer+=1
print(answer)