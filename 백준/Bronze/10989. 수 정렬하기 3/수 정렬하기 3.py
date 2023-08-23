import sys
c = [0]*10000
n = int(sys.stdin.readline())
for _ in range(n):
    c[int(sys.stdin.readline())-1] +=1
for i in range(10000):
    if c[i]>=0:
        for j in range(c[i]):
            print(i+1)