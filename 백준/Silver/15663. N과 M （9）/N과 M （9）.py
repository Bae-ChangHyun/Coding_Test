import sys
input = sys.stdin.readline

n, m =  map(int,input().split())
array = sorted([*map(int,input().split())])

def dfs():
    if len(s) == m :
        print(' '.join(map(str,s)))
        return 
    prev = None  # added
    for i in range(len(array)):
        if visited[i]==1: continue
        if prev is not None and prev == array[i]: continue  # added
        visited[i]=1
        s.append(array[i])
        prev = array[i]  # added
        dfs()
        s.pop()
        visited[i]=0
        
s = []
visited = [0]*(len(array))
dfs()