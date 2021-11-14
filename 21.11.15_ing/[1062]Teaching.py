n,k=map(int,input().split())
sum=0
tmp2=[]

for i in range(n):
    tmp=input()
    #tmp=[i for i in set(tmp[4:-4])]
    tmp=[i for i in set(tmp)]
    tmp.remove('a')
    tmp.remove('n')
    tmp.remove('t')
    tmp.remove('i')
    tmp.remove('c')
    tmp2+=tmp
    if(len(tmp)<=k-5):
        sum+=1
if(sum>k-5):
    
        