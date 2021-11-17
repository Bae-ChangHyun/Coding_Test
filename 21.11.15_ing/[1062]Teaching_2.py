from itertools import combinations
n,k=map(int,input().split())
word=[]
letter=[]
cnt=0

if(k<5):
    print(0)
else:
    for i in range(n):
        tmp=input()
        tmp=[i for i in set(tmp)]
        tmp.remove('a') 
        tmp.remove('n')
        tmp.remove('t')
        tmp.remove('i')
        tmp.remove('c')
        for j in tmp:
            letter.append(j)
        tmp="".join(tmp)
        word.append(tmp)       

result=[0]
for i in range(len(word),0,-1):
     for j in combinations(word,i):
        tmp=""
        for l in j:
            if(l not in tmp):
                tmp+=l
        if(len(tmp)<=k-5):
            result.append(i)
        if(len(result)==2):
            break
     if(len(result)==2):
            break 
print(result)