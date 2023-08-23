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