n,m,k=map(int,input().split())
t=0

while(1):
    if(n>=2 and m>=1):
        n,m=n-2,m-1
        if(n+m>=k):
            t+=1
        else:
            print(t)
            break
    else:
        print(t)
        break