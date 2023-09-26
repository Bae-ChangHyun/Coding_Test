import math
import sys
input = sys.stdin.readline

n = int(input())
c = 0
answer = 0

while (n != 0):
    if (c + 1 > n):
        c = 1
    else:
        c += 1
    n -= c
    answer += 1
print(answer)
