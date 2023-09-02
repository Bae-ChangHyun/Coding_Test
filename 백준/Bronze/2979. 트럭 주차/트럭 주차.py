import sys
input=sys.stdin.readline

answer=0

price=list(map(int,input().split()))
count_list=[0 for i in range(100)]

for i in range(3):
    a,b=map(int,input().split())
    for j in range(a,b):
        count_list[j]+=1
        
for i in range(3):
    answer+=price[i]*(count_list.count(i+1))*(i+1)
print(answer)