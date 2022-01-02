tmp,res=[],0
n,k=map(int,input().split())
for i in range(n):
    a=int(input())
    if(a<=k):
        tmp.append(a)
for i in range(len(tmp)-1,-1,-1):
    res+=k//tmp[i]
    k%=tmp[i]
print(res)

'''
i=-1
while(k!=0):
    if(k>=tmp[i]):
        k-=tmp[i]
        res+=1
    else:
        i-=1
'''

        
