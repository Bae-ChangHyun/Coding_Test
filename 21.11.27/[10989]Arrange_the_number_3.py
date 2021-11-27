import sys
c = [0]*10001
n = int(sys.stdin.readline())
for _ in range(n):
    c[int(sys.stdin.readline())]+=1
for i in range(10001):
    for j in range(c[i]):
        print(i)