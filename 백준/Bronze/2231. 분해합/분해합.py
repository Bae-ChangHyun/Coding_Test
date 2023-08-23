import sys
input=sys.stdin.readline

n=int(input())
result=[]


for i in range(1,n):
    tmp=i
    for j in str(i):
        tmp+=int(j)
    if(tmp==n):
        result.append(i)
if(result==[]):result.append(0)    
print(min(result))