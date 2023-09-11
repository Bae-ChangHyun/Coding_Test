import sys
input=sys.stdin.readline


n=int(input())
a=1
answer=0
while(1):
    answer+=a
    if(answer>n):break
    a+=1
print(a-1)