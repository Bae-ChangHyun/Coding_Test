cnt,sums=0,0
tmp=input()
while("()" in tmp):
    tmp=tmp.replace("()","L")


for i in range(len(tmp)):
    if(tmp[i]=='('):
        for j in range(i+1,len(tmp)):
            if(tmp[j]=='('):
                break
            elif(tmp[j]==')'):
                sums+=tmp[i:j+1].count('L')+1
                tmp=tmp[:i]+'D'+tmp[i+1:]
                tmp=tmp[:j]+'D'+tmp[j+1:]
                break
    if(tmp[j]==')'):
        for j in range(i,-1,-1):
            if(tmp[j]=='('):
                sums+=tmp[j:i+1].count('L')+1
                tmp=tmp[:i]+'D'+tmp[i+1:]
                tmp=tmp[:j]+'D'+tmp[j+1:]
                break
#print(tmp)
print(sums)