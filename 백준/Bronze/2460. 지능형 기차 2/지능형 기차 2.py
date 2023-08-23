arr=[]
people,max=0,0
for i in range(10):
    a,b=input().split()
    arr.append(int(a))
    arr.append(int(b))
for idx,i in enumerate(arr):
    if(idx%2==0):
        people-=i
    else:
        people+=i
    if(max<people):
        max=people
print(max)