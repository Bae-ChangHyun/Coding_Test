"""
import sys
input = sys.stdin.readline

t=int(input())
for i in range(t):
    cursor,answer,code=0,"",[]
    tmp=input().rstrip()
    for i in tmp:
        box=[]
        cnt=0
        if(i.isalpha() or ((i>='0') and (i<='9'))):
            box=code[cursor:]
            code=code[:cursor]
            code.append(i)
            code+=box
            if(box!=[]):
                cursor-=1
            cursor+=1
        else:
            if(i=='-'):
                if(code):code.pop()
            else:
                if(code):
                    if(i=='>'):cursor+=1
                    else:cursor-=1                 
    for i in code:answer+=i
    print(answer)          
"""
from collections import deque
T = int(input())
for _ in range(T):
    L = input()
    left = deque()
    right = deque()
    for i in L:
        if(i=="<"):
            if(len(left)!=0):
                right.appendleft(left.pop())
        elif(i==">"):
            if(len(right)!=0):
                left.append(right.popleft())
        elif(i=="-"):
            if(len(left)!=0):
                left.pop()
        else:
            left.append(i)
    print(''.join(left+right))