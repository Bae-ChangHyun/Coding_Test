import sys
input=sys.stdin.readline

a=input()
n_temp=[]
c_temp=['/n']
temp=''

for i in range(len(a)):
    if(a[i]!='+' and a[i]!='-' and i!=len(a)-1):
        temp+=a[i]
    else:
        if(c_temp[-1]=='+'):
            n_temp[-1]+=int(temp)
        else:
            n_temp.append(int(temp))
        temp=''
        c_temp.append(a[i])

for i in range(len(n_temp)-1):
    n_temp[i+1]=(n_temp[i]-n_temp[i+1])

print(n_temp[-1])