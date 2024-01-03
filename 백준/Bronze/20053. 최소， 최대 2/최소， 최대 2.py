import sys
input=sys.stdin.readline

"""
sort->시간복잡도:O(NlogN)
min,max-> 시간복잡도:O(N)
"""

T=int(input())
for i in range(T):
    N=int(input())
    num=list(map(int,input().split()))
    #num.sort()
    #print(num[0],num[-1])
    print(min(num),max(num))