from itertools import combinations
n,k=map(int,input().split())
strA,strB="",""
tmp2=dict()
total,result=[],[] #입력받은 문장에서 필요한 단어의 전체 조합 
m,sumtmp,maxsum=0,0,0

for i in range(n):
    tmp=input()
    tmp=[i for i in set(tmp)] #중복은 의미없기 때문에 집합으로 지워버림
    # 반드시 알아야 하는 문자5개 미리 없애줌 
    tmp.remove('a') 
    tmp.remove('n')
    tmp.remove('t')
    tmp.remove('i')
    tmp.remove('c')
    strA="".join(tmp) #알아야 하는 문자를 문자열 형태로 표현 ex)['A','B']->'AB'
    if(len(strA)>1):
        ptm=list(combinations(tmp,len(tmp))) #ptm에 tmp로 만들 수 있는 조합들을 모두 넣음
        for j in ptm:
            strB="".join(j) #문자열로 변환 
            if(strB in tmp2): #이미 있는 형태면 만들 수 있는 문장의 개수 +1
                tmp2[strB]+=1
                break
            else:
                if(strB==strA): #처음보는 조합이면 1
                    tmp2[strB]=1 
    else:
        if(strA in tmp2):
            tmp2[strA]+=1
        else:
            tmp2[strA]=1 
# 위 코드까지 했으면 tmp2에 각문자로 만들 수 있는 단어의 개수가 딕셔너리 형태로 들어있음
for i in tmp2:
    for j in tmp2:
        if(i!=j and j in i):
            tmp2[i]+=tmp2[j]
#위 반복문은 예를 들어 kof를 배우면 k,o,f각각으로 배울수 있는 단어 합친거 
#print(tmp2)
ptm=[]
# 이 3중 반복문+조합을 수정해보자 
for i in range(1,len(tmp2)+1):
    ptm=list(combinations(tmp2.keys(),i)) 
    for j in ptm:
        etx=set([t for t in ptm.split()])
        print(etx)
        for t in j:
            m+=len(t)    
        if(m==k-5):
            for l in j:
                result.append(l)
            total.append(result)
            result=[]
        m=0
    ptm=[]
#print(total)
#print(tmp2)
for i in total:
    for j in i:
        sumtmp+=tmp2[j]
    maxsum=max(maxsum,sumtmp)
    sumtmp=0
print(maxsum)

