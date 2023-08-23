import sys
input = sys.stdin.readline

n=int(input())
price=[int(input()) for i in range(n)]
price.sort(reverse=True)
answer=[]
result=0

for i in range(0,n-2,3):
    answer.append(price[i:i+3])
answer.append(price[i+3:])

for i in answer:
    if(len(i)==3):
        result+=sum(i)-min(i)
    else:
        result+=sum(i)
#print(answer)
print(result)