import sys
input=sys.stdin.readline

n=int(input())
a=input()
cnt=0
temp=[a[0]]

for i in range(1,len(a)):
    if(a[i]!=temp[-1] and a[i]!='\n'):
        temp.append(a[i])
        
b=temp.count('B')
r=temp.count('R')
         
for i in range(1,len(a)):
    if(a[i]!=a[i-1]):cnt+=1

answer=min(min(b,r)+1,cnt)
print(answer)