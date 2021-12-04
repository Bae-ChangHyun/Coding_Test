import sys
import string

tmp=list(map(int,sys.stdin.readline().split()))
upper=[j for j in string.ascii_uppercase]
table,result=dict(),""

for i in range(10,36):
    table[i]=upper[i-10]
while(tmp[0]!=0):
    a=tmp[0]%tmp[1]
    tmp[0]=tmp[0]//tmp[1]
    if(a>=10):
        result+=table[a]
    else:
        result+=str(a)
print(result[::-1])

"""
N,B=map(int, input().split())
r=''
while N!=0:
    N,m=N//B,N%B
    if m>9: r=chr(m+55)+r
    else: r=str(m)+r
print(r)

n,b=map(int,input().split())
r=''
while n:
    r=chr(n%b+48+(n%b>9)*7)+r
    n//=b
print(r)
"""