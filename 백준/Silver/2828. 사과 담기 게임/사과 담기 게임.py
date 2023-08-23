
#! [내 답안]
n,m=map(int,input().split())
num=int(input())

start=1
end=start+m
answer=0

for i in range(num):
    a=int(input())
    if(a>=start and a<end):pass
    elif(a<start):
        answer+=start-a
        start=a
        end=start+m
    else:
        answer+=a+1-end
        end=a+1
        start=end-m
print(answer)