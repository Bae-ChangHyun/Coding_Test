import sys
m,n=map(int,sys.stdin.readline().split())
tmp=[i for i in range(2,n+1)]
for idx,i in enumerate(tmp):
    if(i!=0):
        for j in range(idx+i,len(tmp),i):
            tmp[j]=0
for i in tmp:
    if(i>=m):
        print(i)