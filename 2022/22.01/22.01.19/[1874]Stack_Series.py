import sys
input=sys.stdin.readline

n=int(input())
stack1,stack2=[],[]
# push하는 리스트, 정답과 비교할 최종리스트
answer,tmp=[],[] 
# 입력받는수열, +-저장하는 리스트 
index=0

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