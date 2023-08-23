tmp,tmp2,sum=[],[],0
a=input()
a=[i for i in a]
# 완전한 괄호인지 확인하는 코드
for i in a:
    if(tmp==[]):
        tmp.append(i)
        continue
    if(i=='(' or i=='['):
        tmp.append(i)
    elif(i==')'):
        if(tmp[-1]=='('):
            tmp=tmp[:-1]
        else:
            tmp.append(i)
    else:
        if(tmp[-1]=='['):
            tmp=tmp[:-1]
        else:
            tmp.append(i)
if(len(tmp)!=0):
    print(0)
else:
    for i in a:
        if(tmp2==[]):
            tmp2.append(i)
            continue
        if(i=='(' or i=='['):
            tmp2.append(i)
        elif(i==')'):
            if(tmp2[-1]=='('):
                tmp2=tmp2[:-1]
                tmp2.append('2')
            else:
                tmp2.append(i)
        else:
            if(tmp2[-1]=='['):
                tmp2=tmp2[:-1]
                tmp2.append('3')
            else:
                tmp2.append(i)
    while(len(tmp2)!=1):
        for i in range(len(tmp2)-1):
            if(tmp2[i].isdigit()):
                if(tmp2[i-1]=='(' and tmp2[i+1]==')'):
                    tmp2[i]=str(int(tmp2[i])*2)
                    tmp2[i-1]='0'
                    tmp2[i+1]='0'
                elif(tmp2[i-1]=='[' and tmp2[i+1]==']'):
                    tmp2[i]=str(int(tmp2[i])*3)
                    tmp2[i-1]='0'
                    tmp2[i+1]='0'
                elif(tmp2[i+1].isdigit()):
                    tmp2[i]=str(int(tmp2[i])+int(tmp2[i+1]))
                    tmp2[i+1]='0'
        while(tmp2.count('0')!=0):
            tmp2.remove('0') 
    print(int(tmp2[0]))
    
            
