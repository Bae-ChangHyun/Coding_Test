from itertools import permutations

min,max=1000000000,-1000000000 
n=int(input()) #입력할 숫자의 개수

nums=list(map(int,input().split())) #계산할 숫자들
tmp=list(map(int,input().split())) #연산자들의 개수

op='+'*tmp[0]+'-'*tmp[1]+'*'*tmp[2]+'/'*tmp[3] 
op=[i for i in op] #연산자 리스트

allop=list(permutations(op, sum(tmp))) #연산자 순열

for i in allop:
    sum=nums[0]
    for j in range(1,len(nums)):
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