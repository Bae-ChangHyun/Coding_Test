def delete(cnt,tmp,n):
    for i in range(n//3,cnt,n):
        for t in range(i,i+n//3,1):
            for j in range(n//3,cnt,n):
                tmp[t]=tmp[t][:j]+" "*(n//3)+tmp[t][j+(n//3):]
    if(cnt!=n):
        return delete(cnt,tmp,n*3)
    else:
        return tmp

n=int(input())
tmp= ['*'*n for _ in range(n)]

tmp=delete(n,tmp,3)
    
for i in tmp:
    print(i)