import sys
import math
input=sys.stdin.readline

N,K= map(int,input().split())
answer=[]

for i in range(1,int(math.sqrt(N))+1):
    if(N%i==0):
        answer.append(i)
        answer.append(N//i)
answer=list(set(answer))
answer.sort()
if(len(answer)<K):print(0)
else:(print(answer[K-1]))
    