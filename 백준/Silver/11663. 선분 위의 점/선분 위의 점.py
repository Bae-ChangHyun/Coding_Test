import sys
input = sys.stdin.readline

n, m = map(int, input().split())
point = list(map(int, input().split()))
point.sort()
line=[map(int,input().split()) for i in range(m)]

def binary_min(start, end, target):
    while start <= end:
        idx = (start + end) // 2
        mid = point[idx]
        
        if target > mid:
            start = idx + 1
        else:
            end = idx - 1
    return end + 1

def binary_max(start, end, target):
    while start <= end:
        idx = (start + end) // 2
        mid = point[idx]

        if target >= mid:
            start = idx + 1 
        else:
            end = idx - 1
    return end

for least, largest in line:
    start, end  = 0, len(point)-1 # index
    mini = binary_min(start, end, least)
    maxi = binary_max(start, end, largest)
    print(maxi - mini + 1)