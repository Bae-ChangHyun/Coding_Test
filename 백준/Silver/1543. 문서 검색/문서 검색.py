import math
import sys
input = sys.stdin.readline

doc = input().rstrip()
search = input().rstrip()
i, cnt = 0, 0

while (1):
    if (i+len(search) > len(doc)):
        break
    if (doc[i] == search[0]):
        if (doc[i:i+len(search)] == search):
            cnt += 1
            i += len(search)-1
    i += 1
print(cnt)
