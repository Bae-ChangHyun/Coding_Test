import sys
input = sys.stdin.readline

n, m =  map(int,input().split())
array = sorted([*map(int,input().split())])

def dfs():
    if len(s) == m :
        print(' '.join(map(str,s)))
        return 
    for i in range(len(array)):
        if visited[array[i]] == m: continue
        visited[array[i]] += 1
        s.append(array[i])
        dfs()
        s.pop()
        visited[array[i]]-=1
        
s = []
visited = [0]*(max(array)+1)
dfs()