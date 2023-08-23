import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dna,answer=[],""
hm=0
 
for i in range(n):
    dna.append(input().rstrip())

for i in range(m):
    tmp=dict()
    for j in dna:
        if(j[i] in tmp):
            tmp[j[i]]+=1
        else:
            tmp[j[i]]=1
    tmp=sorted(tmp.items(), key=lambda x: (-x[1],x[0]))
    answer+=tmp[0][0]
    hm+=n-tmp[0][1]
print(answer,hm)