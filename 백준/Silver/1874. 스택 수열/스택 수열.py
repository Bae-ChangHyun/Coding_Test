import sys
input=sys.stdin.readline

n=int(input())
stack1=[] # 뭔
stack2=[] # 맨마지막에 해줄 리스트
index=0
answer=[] # 우리가 만들고자 하는 리스트 
tmp=[] #부호 저장하는 리스트

for i in range(n):
    answer.append(int(input()))
for i in range(n):
    stack1.append(i+1)
    tmp.append('+')
    for j in range(len(stack1)-1,-1,-1):
        if(stack1[j]==answer[index]):
            tmp.append('-')
            a=stack1.pop()
            stack2.append(a)
            index+=1
        else:
            break
if(stack2==answer):
    print(*tmp)
else:
    print("NO")   