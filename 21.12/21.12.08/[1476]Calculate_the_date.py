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

"""
e, s, m = map(int, input().split())
a = (6916 * e + 4845 * s + 4200 * m) % 7980
print(a if a else 7980)
"""