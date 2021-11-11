'''
a,b=input().split()
a=int(a)
b=int(b)
tmp=[]
sum=0

for i in range(b):
    if(len(tmp)>b):
        break
    while(tmp.count(i+1)!=i+1):
        if(len(tmp)>b):
            break
        tmp.append(i+1)
for i in range(a-1,b):
    sum+=tmp[i]
print(sum)
'''
a,b=map(int,input().split())
print(sum(int(1+(8*n)**.5)//2 for n in range(a,b+1)))