"""
import sys
from itertools import permutations
input=sys.stdin.readline

n,k=map(int,input().split())
num=list(input().split())*len(str(n))
k=len(str(n))
result=[]

for i in range(1,k+1):
    for j in permutations(num,i):
        tmp=int(''.join(j))
        if(tmp<=n):
            result.append(tmp)
print(max(result))

"""
from itertools import product

n, k = map(int, input().split())
arr = list(map(str, input().split()))
length = len(str(n))

while True:
    temp = list(product(arr, repeat=length))  # repeat을 통해 몇개를 뽑을지 설정한다.
    ex = []
    for i in temp:
        now=int(''.join(i))
        if now <= n:
            ex.append(now)
    if len(ex) >= 1:
        print(max(ex))
        break
    else:
        length -= 1
