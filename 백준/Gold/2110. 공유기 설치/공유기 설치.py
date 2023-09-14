import sys
input = sys.stdin.readline

N, C = map(int,input().split())
array = [int(input()) for _ in range(N)]
array.sort() 

start = 1 
end = array[-1] - array[0]
answer = 0

while start <= end :
    now = array[0]
    cnt = 1 
    mid = (start+end) // 2
    for i in range(1,N) :
        if (array[i] - now >= mid ) :
            cnt += 1
            now = array[i]
    if cnt >= C :
        if answer < mid : 
            answer = mid
        start = mid + 1
    else :
        end = mid - 1

print(answer)