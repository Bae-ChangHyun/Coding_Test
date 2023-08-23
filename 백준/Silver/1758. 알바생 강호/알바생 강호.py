import sys
input = sys.stdin.readline

n=int(input())
tip=[]

for i in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)
answer=[i[1]-(i[0]) for i in enumerate(tip) if i[1]-i[0]>0]

print(sum(answer))
