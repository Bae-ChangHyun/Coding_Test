import sys
input=sys.stdin.readline

n=int(input())
tip,get=[],0

for i in range(n):
    tip.append(int(input()))
tip.sort(reverse=True)
for i in range(len(tip)):
    a=tip[i]-i
    if(a>=0):get+=a
print(get)