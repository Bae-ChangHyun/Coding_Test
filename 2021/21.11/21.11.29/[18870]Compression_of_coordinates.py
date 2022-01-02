'''
RuntimeError
import sys
n=int(sys.stdin.readline())
tmp,b=[0]*2000000001,[]
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
'''
import sys
input =sys.stdin.readline 
n = int(input())
arr = list(map(int,input().split())) 
s = list(sorted(set(arr))) 
dic={value:index for index,value in enumerate(s)} 
for i in arr: 
	print(dic[i],end=" ")
