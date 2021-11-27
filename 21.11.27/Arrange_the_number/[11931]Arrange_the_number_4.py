import sys
n=int(input())
tmp=[]
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))
tmp.sort(reverse=True)
for i in tmp:
    print(i)
