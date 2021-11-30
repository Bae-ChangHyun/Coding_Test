'''
a=int(input())
b=int(input())
tmp=[]

tmp=[i for i in range(b+1)]
for i in range(2,len(tmp)):
    for j in range(i*2,len(tmp),i):
        tmp[j]=0
tmp=[i for i in tmp[a:] if(i!=0)]
if(1 in tmp):
    tmp.remove(1)
if(tmp!=[]):
    print(sum(tmp))
    print(min(tmp))
else:
    print(-1)
'''
a = int(input())
b = int(input())
c = [i for i in range(a,b+1) if i != 1 and all(i % j for j in range(2,i))]
if c:
    print(sum(c))
    print(c[0])
else:
    print(-1)

        
    
    
