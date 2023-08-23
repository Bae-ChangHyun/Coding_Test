import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    tmp=dict()
    code=input().rstrip()
    for j in code:
        if(j!=" "):
            if(j not in tmp):
                tmp[j]=1
            else:
                tmp[j]+=1
    tmp=sorted(tmp.items(), key=lambda x:-x[1])
    if(len(tmp)==1):print(tmp[0][0])
    elif(tmp[0][1]==tmp[1][1]):
        print("?")
    else:print(tmp[0][0])