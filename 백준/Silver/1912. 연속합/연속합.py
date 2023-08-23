import sys
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
answer=[]
a=0

for i in range(n):
    if(num[i]>0):
        a+=num[i]
        answer.append(a)
    else:
        a+=num[i]
        if(a<0):
            answer.append(num[i])
            a=0
        else:
            answer.append(a)
    
#print(answer)
print(max(answer))