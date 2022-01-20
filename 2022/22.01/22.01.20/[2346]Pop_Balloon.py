import sys
input=sys.stdin.readline

n=int(input())
ball=list(map(int,input().split()))
index=[i+2 for i in range(n-1)]
result=[1]

i=0
a=ball.pop(i)


while(len(ball)!=0):
    if(a>0):
        i=(i-1+a)%len(ball)
    else:
        i=(i+a+len(ball))%len(ball)
    a=ball.pop(i)
    b=index.pop(i)
    result.append(b)
print(*result)