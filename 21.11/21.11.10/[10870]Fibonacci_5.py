'''
n=int(input())
pnum=[0,1]
if(n<2):
    print(pnum[n])
else:   
    for i in range(2,n+1):
        pnum.append(pnum[i-2]+pnum[i-1])
    print(pnum[-1])
'''
a,b=0,1
for i in range(int(input())):
    a,b=a+b,a
print(a)   