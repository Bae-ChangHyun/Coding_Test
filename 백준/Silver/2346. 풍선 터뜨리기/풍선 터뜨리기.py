import sys
input=sys.stdin.readline

n=int(input())
ball=list(map(int,input().split()))
index=[i+2 for i in range(n-1)] #1을제외한 이후 인덱스만 넣어줌
result=[1] #1은 제일 먼저 터뜨리므로 미리 넣어둠

i=0
a=ball.pop(i) #첫번째 풍선 터뜨림

while(len(ball)!=0):
    if(a>0):
        i=(i-1+a)%len(ball) #쪽지수가 양수일경우
    else:
        i=(i+a+len(ball))%len(ball) #쪽지수가 음수일 경우
    a=ball.pop(i) #풍선을 터뜨림
    b=index.pop(i) #해당 풍선 원래 인덱스
    result.append(b) #풍선인덱스를 결과값에 저장
print(*result)