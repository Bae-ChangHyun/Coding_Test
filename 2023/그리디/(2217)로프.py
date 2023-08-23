
#? 백준[2217]_로프_(그리디 연습문제)
#! [모범 답안]
n=int(input())
maximum=sorted([int(input()) for _ in range(n)],reverse=True)
w=[maximum[i]*(i+1) for i in range(n)]
print(max(w))

#! [내 답안]
import sys
input = sys.stdin.readline

rope=[]
n=int(input())
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
answer=[(i[0]+1)*i[1] for i in enumerate(rope)]
print(max(answer))


