import sys
input = sys.stdin.readline

N = int(input())
bud = list(map(int, input().split()))
M = int(input())

# 전체 요청액이 예산 이하이면 최대 요청액을 그대로 출력
if sum(bud) <= M:
    print(max(bud))
    sys.exit(0)

low, high = 0, max(bud)
answer = 0

while low <= high:
    mid = (low + high) // 2          # 현재 후보 상한값
    total = sum(min(b, mid) for b in bud)   # 상한값을 적용했을 때의 합

    if total <= M:                   # 예산을 초과하지 않으면 더 크게 시도
        answer = mid
        low = mid + 1
    else:                            # 초과하면 상한값을 낮춘다
        high = mid - 1

print(answer)