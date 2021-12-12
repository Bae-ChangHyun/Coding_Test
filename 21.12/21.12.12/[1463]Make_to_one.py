n=int(input())

d=[0]*(n+1)
d[1]=0

for i in range(2,n+1):
    tmpa,tmpb=n,n
    if(i%2==0):
        tmpa=d[i//2]+1
    if(i%3==0):
        tmpb=d[i//3]+1
    tmpc=d[i-1]+1
    d[i]=min(tmpa,tmpb,tmpc)
    print(i,d[i])
print(d[n])

