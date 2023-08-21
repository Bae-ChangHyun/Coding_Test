N,M,K=map(int, input().split())
num=list(map(int, input().split()))

num.sort()

b=M%K 
a=M-b
answer=num[-1]*a+num[-2]* b 

print(answer)


# count = int(M/(K+1)) * k
# count += M % (K+1)
# result = 0
# result += (count) * first
# result += (M - count) * second
# print(result) 
