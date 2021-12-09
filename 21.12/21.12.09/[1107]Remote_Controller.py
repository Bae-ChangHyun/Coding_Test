t=str(int(input())-100)
n=input()
tmp=list(map(int,input().split()))
tmp2=[i for i in range(0,10)]
for i in range(len(tmp2)):
    if(tmp2[i] in tmp):
        tmp2[i]=0
tmp=""
print(t)
# 남은 번호중에 t와 가장 가장 가깝게 만들어야됨.
flag=0
if(t=='0'):
    print(0)
else:
    for i in t:
        if(flag==0):
            a=max(tmp2[:int(i)+1])
        else:
            a=max(tmp2)
            flag=0
        if(a<int(i)):
            flag==1
        tmp+=str(a)
    print(tmp)
    print(len(tmp)+int(t)-int(tmp))
    
