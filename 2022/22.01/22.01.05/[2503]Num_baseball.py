import sys
input=sys.stdin.readline

n=int(input())
num=[i for i in range(100,1000)]
cnt=0

for i in range(n):
    res,ts,tb=map(int,input().split())
    for j in range(len(num)):
        ans,bns=0,0
        tmp=str(num[j])
        #print(tmp)
        #각 자릿수가 달라야함
        if(tmp=='0'):
            continue
        if((tmp[0]==tmp[1] or tmp[0]==tmp[2] or tmp[1]==tmp[2]) or ('0' in tmp)):
            num[j]=0
        else:
            res=str(res)
            for k in range(3):
                for l in range(3):
                    if(tmp[k]==res[l] and k==l):
                        ans+=1
                    elif(tmp[k]==res[l] and k!=l):
                        bns+=1
            #print(num[j],ans,bns)
            if(ans!=ts or bns!=tb):
                num[j]=0

print(900-num.count(0))