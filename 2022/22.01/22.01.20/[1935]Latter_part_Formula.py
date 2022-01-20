def calc(a,b,c):
    if(c=='+'):return a+b
    if(c=='-'):return a-b
    if(c=='*'):return a*b
    if(c=='/'):return a/b

import sys
input=sys.stdin.readline

n=int(input())
f=input().rstrip()
stack=[]
board=dict()

for i in f:
    if(i.isalpha() and i not in board):
        board[i]=int(input())
        
for i in f:
    if(i.isalpha()):
        stack.append(board[i])
    else:
        a=stack.pop()
        b=stack.pop()
        a,b=b,a
        stack.append(calc(a,b,i))
print("%.2f"%stack[-1]) 