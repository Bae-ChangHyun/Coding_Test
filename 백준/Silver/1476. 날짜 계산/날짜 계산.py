e,s,m=list(map(int,input().split()))
if(e==15):e-=15
if(s==28):s-=28
if(m==19):m-=19
n=1
while(1):
    if(n%15==e and n%28==s and n%19==m):
        print(n)
        break
    else:n+=1
    