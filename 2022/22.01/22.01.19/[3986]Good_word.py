import sys
input=sys.stdin.readline

cnt=0
n=int(input())
for i in range(n):
    stack=[]
    tmp=input().rstrip()
    tmp=[j for j in tmp]
    for k in tmp:
        if(stack==[]):
            stack.append(k)
        else:
            if(stack[-1]==k):
                stack.pop()
            else:
                stack.append(k)
        #print(stack)
        
    if(stack==[]):cnt+=1
print(cnt)
