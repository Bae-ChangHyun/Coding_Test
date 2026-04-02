import sys
input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
m = int(input())

# 전체 요청액이 예산 이하이면 그대로 지급
if sum(requests) <= m:
    print(max(requests))
    sys.exit(0)

def find_cap(arr, limit):
    start, end = 0, max(arr)          # 가능한 상한값 범위
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        total = sum(min(x, mid) for x in arr)

        if total <= limit:            # 현재 mid 로도 예산을 초과하지 않음
            answer = mid              # 후보 저장
            start = mid + 1           # 더 큰 값을 시도
        else:
            end = mid - 1             # 중간값이 너무 큼
    return answer

print(find_cap(requests, m))