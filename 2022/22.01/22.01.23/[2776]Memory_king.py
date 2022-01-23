import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n1=int(input())
    note1=list(map(int,input().split()))
    n2=int(input())
    note2=list(map(int,input().split()))
    result=set(note1)&set(note2)
    for j in note2:
        if(j in result):print(1)
        else:print(0)
    