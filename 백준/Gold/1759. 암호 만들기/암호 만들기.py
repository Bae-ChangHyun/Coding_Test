from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
letter = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']

a = list(combinations(letter, L))
a = ["".join(sorted(i)) for i in a]


for i in sorted(a):
    cnt = 0
    for j in vowels:
        if (j in i):
            cnt += 1
    if (len(i)-cnt >= 2 and cnt >= 1):
        print(i)