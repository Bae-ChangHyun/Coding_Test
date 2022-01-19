import sys
input=sys.stdin.readline

while(1):
    flag=1
    stack=[]
    tmp=input().rstrip()
    if(tmp=='.'):break
    tmp=[i for i in tmp]
    for i in tmp:
        if(i.isalpha() or i=='.' or i==' '):continue
        else:
            if(i in ['(','[']):
                stack.append(i)
            else:
                if(stack==[]):
                    flag=0
                    break
                if(i==')'):
                    if(stack[-1]=='('):
                        stack.pop()
                    else:
                        flag=0
                        break
                if(i==']'):
                    if(stack[-1]=='['):
                        stack.pop()
                    else:
                        flag=0
                        break
    if(flag and stack==[]):print("yes")
    else:print("no")