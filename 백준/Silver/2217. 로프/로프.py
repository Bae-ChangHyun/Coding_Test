import sys
input = sys.stdin.readline

rope=[]
n=int(input())
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
answer=[(i[0]+1)*i[1] for i in enumerate(rope)]
print(max(answer))