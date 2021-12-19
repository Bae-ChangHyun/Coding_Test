def find_cnt(num,cnt,time,n):
    res=0
    if(time==n):return cnt
    if(num==0 or num==9):
        res+=find_cnt(n+1,cnt*1,time+1,n) 
    else:
        tmp=cnt
        res+=find_cnt(n-1,cnt*2,time+1,n)
        res+=find_cnt(n+1,tmp*2,time+1,n)
    
    return res

n=int(input())
tmp=0

for j in range(1,10):
    tmp+=find_cnt(j,1,1,n)
    print(j,tmp)
print(tmp)
            

    