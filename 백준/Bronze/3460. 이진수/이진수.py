k=int(input())
for i in range(k):
    N=int(input())
    tmp=bin(N)[2:]
    result=[len(tmp)-1-i for i in range(len(tmp)) if(tmp[i]=='1')]
    result.reverse()
    for i in result: print(i,end=" ")
    tmp=[]
    result=[]


