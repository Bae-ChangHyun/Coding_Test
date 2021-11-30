'''
n=int(input())
result=0
tmp=list(map(int,input().split()))

for i in tmp:
    cnt=0
    for j in range(1,i+1):
        if(i%j==0):
            cnt+=1
    if(cnt==2):
        result+=1
print(result) 
'''
input()
print(sum(all(i%j for j in range(2,i))for i in map(int,input().split())if i>1))
        
