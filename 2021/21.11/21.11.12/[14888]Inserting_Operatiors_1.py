'''
from itertools import permutations

min,max=1000000000,-1000000000 
n=int(input()) #입력할 숫자의 개수
nums=list(map(int,input().split())) #계산할 숫자들
tmp=list(map(int,input().split())) #연산자들의 개수
op='+'*tmp[0]+'-'*tmp[1]+'*'*tmp[2]+'/'*tmp[3] 
op=[i for i in op] #연산자 리스트
allop=list(permutations(op, sum(tmp))) #연산자 순열

for i in allop: #모든조합의 수 반복
    sum=nums[0]
    for j in range(1,len(nums)): #각각의 계산식 
        if(i[j-1]=='+'):
            sum+=nums[j]
        elif(i[j-1]=='-'):
            sum-=nums[j]
        elif(i[j-1]=='*'):
            sum*=nums[j]
        else:
            if(sum<0):
                sum=-((-sum)//nums[j])
            else:
                sum//=nums[j]
    if(sum>max):
        max=sum
    if(sum<min):
        min=sum
print(max)
print(min)
'''
'''
from itertools import permutations
N=int(input())
A=list(map(int, input().split()))
a,s,m,d=map(int, input().split())
l=[]
for p in set(permutations('+'*a+'-'*s+'*'*m+'/'*d)):
    r=A[0]
    for i in range(1,N):
        r={'+':r+A[i],'-':r-A[i],'*':r*A[i],'/':int(r/A[i])}[p[i-1]]
    print(r)
    l.append(r)
print(max(l), min(l))
'''
M=-10**9
m=10**9
N=int(input())
num=list(map(int,input().split()))
a,b,c,d=map(int,input().split())
def inst(n,i,d1,d2,d3,d4):
	global M,m
	if i==N:M=max(M,n);m=min(m,n);return 
	else:
		if d1:inst(n+num[i],i+1,d1-1,d2,d3,d4)
		if d2:inst(n-num[i],i+1,d1,d2-1,d3,d4)
		if d3:inst(n*num[i],i+1,d1,d2,d3-1,d4)
		if d4:inst(int(n/num[i]),i+1,d1,d2,d3,d4-1)
inst(num[0],1,a,b,c,d)
print(M)
print(m)


