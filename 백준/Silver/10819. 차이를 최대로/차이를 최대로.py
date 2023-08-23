import random
from itertools import permutations

n=int(input())
answer,tanswer,limit=0,0,1
tmp=list(map(int,input().split()))

for i in permutations(tmp,n):
    for j in range(len(i)):
        if(j!=len(i)-1):
            tanswer+=abs(i[j]-i[j+1])
    answer=max(tanswer,answer)
    tanswer=0
print(answer)