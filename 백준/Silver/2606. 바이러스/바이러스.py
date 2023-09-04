import sys
input= sys.stdin.readline

def dfs(new_d):
    for i in new_d:
        if(visited[i]==0):
            visited[i]=1
            dfs(d[i])    
    return True

n=int(input())
connect=int(input())

visited=[0 for i in range(n+1)]
d=[[] for _ in range(n+1)]

for i in range(connect):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
visited[1]=1
dfs(d[1])

answer=visited.count(1)
print(answer-1)