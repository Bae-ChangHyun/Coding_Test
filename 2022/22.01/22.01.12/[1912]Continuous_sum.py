import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
d=[0]*(n)

for i in range(n):
    if num[i] < 0 :
        if d[i] + num[i] > 0:
            d[i] = d[i-1]+num[i]
        else:
            d[i] = num[i]
    else:
        d[i]=d[i-1]+num[i]
    print(d)

print(d)
print(max(d))