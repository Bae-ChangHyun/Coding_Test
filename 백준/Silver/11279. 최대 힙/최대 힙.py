import sys
import heapq
input=sys.stdin.readline

n=int(input())
heap = []

for i in range(n):
    tmp=int(input())
    if(tmp!=0):
        heapq.heappush(heap, (-tmp, tmp))
    else:
        if(heap==[]):
            print(0)
        else:
            result=heapq.heappop(heap)
            print(result[1])