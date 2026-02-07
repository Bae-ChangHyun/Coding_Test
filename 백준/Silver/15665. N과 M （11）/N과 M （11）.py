# https://www.acmicpc.net/problem/15665

import sys
input = sys.stdin.readline

n, m =  map(int,input().split())
array = sorted([*map(int,input().split())])

def dfs():
    if len(s) == m :
        print(' '.join(map(str,s)))
        return 
    prev = None
    for i in range(len(array)):
        if prev != None and prev==array[i]:
            continue
        s.append(array[i])
        prev = array[i]
        dfs()
        s.pop()
s = []
dfs()