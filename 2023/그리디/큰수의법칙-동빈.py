
#! [모범답안]
# n,m,k=map(int,input().split)
# data=list(map(int,input().split()))
# data.sort()

# count = int(M/(K+1)) * k
# count += M % (K+1)
# result = 0
# result += (count) * first
# result += (M - count) * second
# print(result) 

#? 반복되는 수열을 파악하기. 
#? 나동빈 코딩테스트(p.95), 2019 국가 교육기관 코딩 테스트 

#! [내 답안]
N,M,K=map(int, input().split())
num=list(map(int, input().split()))

num.sort()

b=M%K 
a=M-b
answer=num[-1]*a+num[-2]* b 

print(answer)


