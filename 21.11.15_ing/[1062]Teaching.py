from itertools import permutations
n,k=map(int,input().split())
sum=0
strA=""
tmp2=dict()
ptmp=[]

for i in range(n):
    tmp=input()
    #tmp=[i for i in set(tmp[4:-4])]
    #일반적인경우는 그냥 아래처럼 하면됨
    tmp=[i for i in set(tmp)]
    tmp.remove('a')
    tmp.remove('n')
    tmp.remove('t')
    tmp.remove('i')
    tmp.remove('c')
    strA="".join(tmp)
    ptm=list(permutations(tmp,len(tmp)))
    print(ptm)
    for j in ptm:
        strB="".join(j)
        if(strB in tmp2):
            tmp2[strB]+=1
            break
        else:
            if(strB==strA):
                tmp2[strB]=1       
tmp2=sorted(tmp2.values(),reverse=True)
print(tmp2)
for i in range(k-5):
    sum+=tmp2[i]
print(sum)

# 똑같은 방법인데 순열만생각해보자 