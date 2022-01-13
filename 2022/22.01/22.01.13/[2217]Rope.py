import sys
n=int(input())

rope=[0 for _ in range(n)]
result=[]

for i in range(n):
    rope[i]=int(input())
rope.sort()
for i in range(n):
    result.append(rope[i]*(n-i))
print(max(result))