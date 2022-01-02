n=int(input())

d=[0]*(n+1)
d[1]=1

if(n>=2):
    d[2]=2
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
        #print(d[i]%10007)
print(d[n]%10007)

"""
a=b=1
for i in range(int(input())):
	a,b=b,a+b
print(a%10007)
"""