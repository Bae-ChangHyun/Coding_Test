
#? 백준[11508]_2+1 세일_(그리디 연습문제)
#! [모범 답안]
# from sys import stdin
# n=int(input())
# m=list(map(int, stdin.read().split()))
# m.sort(reverse=True)
# cost = 0
# for i in range(n):
#     if(i%3!=2):
#         cost += m[i]
# print(cost)
#! [내 답안]
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
print(result)