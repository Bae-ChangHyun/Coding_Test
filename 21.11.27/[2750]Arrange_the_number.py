import sys
n=int(input())
tmp=[]
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))
tmp.sort()
for i in tmp:
    print(i)
    
# print(*sorted(map(int,[*open(0)][1:])))
