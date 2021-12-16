"""
n=int(input())
d=[0]*(n+1)
d[1]=1
if(n>=2):
    d[2]=3
    for i in range(3,n+1):
        d[i]=d[i-1]+(2*d[i-2])
print(d[n]%10007)
"""
a=b=1
for i in range(int(input())):
	a,b=b,2*a+b
print(a%10007)
