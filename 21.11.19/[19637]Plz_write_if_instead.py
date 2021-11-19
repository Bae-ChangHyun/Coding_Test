rankn,n=map(int,input().split())
all,k=[],-1
for i in range(rankn):
    tmp=input().split() #tmp는 랭크, tmp2는 기준전투력
    all.append(tmp) 
    all[i][1]=int(all[i][1])
all.append(['etc',0])


for i in range(len(all)-1,-1,-1):
    if(i==0):
        all[i][1]=0
        break
    all[i][1]=all[i-1][1]
    

for i in range(n):
    tmp=int(input())
    idx=int((rankn+1)/2) 
    while(1):
        if(tmp>all[idx][1]):
            idx=int(((rankn+1)-idx)/2)
        else:
            idx=int(idx/2) #얘는 fix
        if(k==idx):
            print(all[idx][0])
            break
        k=idx
        #멈추는 조건 설정 
