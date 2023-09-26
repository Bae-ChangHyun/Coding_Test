import math
import sys
input = sys.stdin.readline

n = int(input())
award = [int(input()) for _ in range(n)]

left = [1 for i in range(1, len(award)) if award[i] > max(award[:i])]
award.reverse()
right = [1 for i in range(1, len(award)) if award[i] > max(award[:i])]

print(sum(left)+1)
print(sum(right)+1)
