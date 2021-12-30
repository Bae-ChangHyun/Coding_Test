import sys
input=sys.stdin.readline

n=int(input())
tmp,price=[],[]

for i in range(n):
    tmp.append(list(map(int,input().split())))
tmp.append([0,0])

price=[i[1] for i in tmp]

for i in range(n-1,-1,-1):
    if(i+tmp[i][0]>n):
        price[i]=price[i+1]
        continue
    prev=i+tmp[i][0]
    price[i]=max(price[i]+price[prev],price[i+1])
    
#print(price)
print(max(price))