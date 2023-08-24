import sys
input = sys.stdin.readline

n=int(input())
health=list(map(int, input().split()))
health.sort()
answer=[]

if(n%2==0):
    for i in range(0,n//2):
        answer.append(health[i]+health[n-1-i])
else:
    answer.append(health[-1])
    for i in range(n//2):
        answer.append(health[i]+health[n-2-i])
print(max(answer))