import sys
input = sys.stdin.readline

n=int(input())
drink=list(map(int,input().split()))
drink.sort()

total=drink[-1]
for i in range(len(drink)-1):
    total += drink[i]/2
print(total)