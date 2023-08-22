
#! [모범답안]
# n,k=map(int,input().split())
# result=0

# while True:
#     target=(n//k)*k
#     result+=(n-target)
    
#     if n<k:
#         break
#     result+=1
#     n//=k
# result+=(n-1)
# print(result)
#? 최대한 많이 나누는 것이 최소 횟수를 만족할 수 있음. 
#? 나동빈 코딩테스트(p.96), 2018 E 기업 알고리즘 대회

#! [내 답안]
n,k=map(int,input().split())
cnt=0

while(n!=1):
    if(n%k==0):n/=k
    else:n-=1
    cnt+=1
print(cnt)