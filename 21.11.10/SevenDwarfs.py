'''
arr=[]
for i in range(9):
    arr.append(int(input()))
tmp=sum(arr)-100
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==tmp):
            a,b=arr[i],arr[j]
            arr.remove(a)
            arr.remove(b)
            arr.sort()
            for k in arr:
                print(k)
            exit()
'''

'''
a=[]
for i in range(9):a.append(int(input()))
for i in a:
    b=sum(a)-i-100
    if b in a and i!=b:a.remove(i);a.remove(b);break
a.sort()
for i in a:
    print(i)
'''

import itertools as i
for s in i.combinations(map(int,open(0)),7):
    if sum(s)==100:
        print(*sorted(s));break