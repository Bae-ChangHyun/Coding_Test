import sys
input = sys.stdin.readline

n=int(input())
city=list(map(int,input().split()))
price=list(map(int,input().split()))

answer=0
for i in range(len(city)):
    if(price[i]==min(price[i:-1])):
        answer+=price[i]*sum(city[i:])
        break
    else:
        answer+=price[i]*city[i]
print(answer)