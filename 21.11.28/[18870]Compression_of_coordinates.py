import sys
n=int(sys.stdin.readline())
tmp,b=[0]*2000000002,[]
board=dict()
a=list(map(int,sys.stdin.readline().split()))
for i in a:
    tmp[len(tmp)//2+i]+=1
for idx,i in enumerate(tmp):
    if(i!=0):
        for j in range(i):
            b.append(idx-len(tmp)//2)
idx=-1
for i in b:
    if(i not in board): 
        idx+=1
        board[i]=idx
for i in a:
    print(board[i],end=" ") 
