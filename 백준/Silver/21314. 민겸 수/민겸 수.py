import sys
input=sys.stdin.readline

a=input()[:-1]
temp=[]

max_n=''
min_n=a.split('K')

for i in range(len(a)):
    if(a[i]=='M'):temp.append(a[i])
    else:
        if(temp==[]):max_n+='5'
        else:
            max_n=max_n+'5'+('0'*(len(temp)))
            temp=[]
if(temp!=[]):max_n=max_n+('1'*len(temp))

for i in range(len(min_n)):
    if(min_n[i]!=''):
        min_n[i]='1'+('0'*(len(min_n[i])-1))
min_n='5'.join(min_n)

print(max_n)
print(min_n)