import sys
input = sys.stdin.readline


n = int(input())
h = list(map(int, input().split()))
h.sort()
answer = dict()

for i in range(len(h)//2-1, len(h)//2+1):
    tmp = [abs(j-h[i]) for j in h]
    answer[h[i]] = sum(tmp)
answer = sorted(answer.items(), key=lambda x: (x[1], x[0]))

print(answer[0][0])