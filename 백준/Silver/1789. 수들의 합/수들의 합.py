s=int(input())
n,cnt=0,0

while(1):
    cnt+=1
    n=int(cnt*(cnt+1)/2)
    if(n>s):
        break
print(cnt-1)