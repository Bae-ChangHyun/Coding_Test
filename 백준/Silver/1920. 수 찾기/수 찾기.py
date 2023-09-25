import sys
input = sys.stdin.readline

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(start, end, target):
    if (start > end):
        return 0
    mid = (start+end)//2
    if (n_list[mid] == target):
        return 1
    elif (n_list[mid] > target):
        return binary_search(start, mid-1, target)
    else:
        return binary_search(mid+1, end, target)

for i in m_list:
    print(binary_search(0, len(n_list)-1, i))
