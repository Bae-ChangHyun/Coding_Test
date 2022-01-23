import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for i in range(t):
    order=1
    n,m=map(int,input().split())
    num=deque([i for i in range(0,n)]) #문서 이름
    h=deque(list(map(int,input().split()))) #각 문서의 중요도
    k=num[m] #k는 우리가 몇번째인지 알고자 하는 문서
    while(len(h)!=0):
        a=h[0] #a는 현재 맨앞에 있는 문서
        if(a!=max(h)): #중요도가 제일 높지 않으면
            tmp=h.popleft()
            tmp2=num.popleft()
            h.append(tmp)
            num.append(tmp2)
        else:
            tmp=h.popleft()
            tmp2=num.popleft()
            if(tmp2==k):
                print(order)
                break
            order+=1
        
    
        