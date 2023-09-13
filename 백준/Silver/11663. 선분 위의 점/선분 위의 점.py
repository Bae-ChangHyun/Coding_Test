import sys
input = sys.stdin.readline

n, m = map(int, input().split())
point = list(map(int, input().split()))
point.sort()
line=[map(int,input().split()) for i in range(m)]

def lower_bound(start,end,target):
    while start<=end:
        mid = (start+end)//2
        if point[mid] < target:
            start = mid +1
        else:
            end = mid-1
    return start

def upper_bound(start,end,target):
    while start<=end:
        mid = (start+end)//2
        if point[mid] <= target:
            start = mid +1
        else:
            end = mid-1
    return start

for least, largest in line:
    start, end  = 0, len(point)-1 # index
    mini = lower_bound(start, end, least)
    maxi = upper_bound(start, end, largest)
    #print(mini,maxi)
    print(maxi - mini)