'''
k=int(input())
for i in range(k):
    N=int(input())
    tmp=bin(N)[2:]
    result=[len(tmp)-1-i for i in range(len(tmp)) if(tmp[i]=='1')]
    result.reverse()
    for i in result: print(i,end=" ")
    tmp=[]
    result=[]
'''
'''
k=int(input())
for i in range(k):
    N,idx=int(input()),0
    while N:
        if(N%2):print(idx,end=' ')
        N//=2
        idx+=1
'''
for _ in[0]*int(input()):
   a,b=int(input()),0
   while a:
      if a%2:print(b,end=' ')
      a//=2;b+=1
