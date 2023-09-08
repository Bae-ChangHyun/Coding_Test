import sys
from collections import deque

input = sys.stdin.readline

N=int(input())
graph=[int(input()) for _ in range(N)]
graph.insert(0,0)
visit=[0 for _ in range(N+1)]

def dfs(idx):    
    if(visit[graph[idx]]==0):
        visit[graph[idx]]=1
        tmp.append(graph[idx])    
        dfs(graph[idx])
    else:
        return 0   
    
answer=set()
for i in range(1,N+1):
    visit=[0 for _ in range(N+1)]
    tmp,visit[i]=[i],1
    dfs(i)
    selected=[graph[j] for j in tmp]
    tmp.sort() # 뽑은 첫째 줄 카드
    selected.sort() # 뽑은 두번째 줄 카드
    if(tmp==selected): 
        answer.update([j for j in tmp])
        
print(len(answer))
answer=list(set(answer))
answer.sort()
for i in answer:
    print(i) 