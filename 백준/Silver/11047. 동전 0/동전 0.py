import sys
input = sys.stdin.readline

n,k=map(int,input().split())
sum=0

coin=[int(input()) for i in range(n)]
coin.sort(reverse=True)

for i in coin:
    sum+=k//i
    k%=i
    
print(sum)