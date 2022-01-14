import sys
from itertools import permutations
input=sys.stdin.readline

n=int(input())
k=int(input())
card,result,tmp=[],set(),""

for i in range(n):
    card.append(int(input()))
    
for i in permutations(card,k):
    for j in i:
        tmp+=str(j)
    result.add(int(tmp))
    tmp=""
print(len(result))
