a=[0,1,2,4]+[0]*8

n=int(input())
for i in range(4,12):
    a[i]=a[i-1]+a[i-2]+a[i-3]
for i in range(n):
    tmp=int(input())
    print(a[tmp])
