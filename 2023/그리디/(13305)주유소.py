
#? 백준[13305]_주유소_(그리디 연습문제)
#! [모범 답안]
n=int(input())
d=list(map(int,input().split()))
p=list(map(int,input().split()))
s=0
k=p[0]
for i in range(n-1):
    if p[i]<k:
        k=p[i]
    s+=k*d[i]
print(s)
#! [내 답안]
import sys
input = sys.stdin.readline

n=int(input())
city=list(map(int,input().split()))
price=list(map(int,input().split()))

answer=0
j=0
for i in range(len(price)):
    if(i<j):continue
    for j in range(i+1,len(price)):
        if(price[i]>price[j]):
            break
    answer+=price[i]*sum(city[i:j])
print(answer)
    