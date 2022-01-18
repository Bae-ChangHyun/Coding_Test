size=int(input())
lst=list(map(int,input().split()))
num=int(input())
lst.sort()

cnt=0
for i in range(size):
    if lst[i]>num:
            for j in range(lst[i-1]+1,num+1):
                if j<num:
                    cnt+=lst[i]-num
                elif j==num:
                    cnt+=lst[i]-num-1 #[n,n]이라는 구간은 없기때문에
            break

print(cnt)