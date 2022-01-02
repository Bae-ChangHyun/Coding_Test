s=int(input())
n,cnt=0,0

while(1):
    cnt+=1
    n=int(cnt*(cnt+1)/2)
    if(n>s):
        break
print(cnt-1)

"""
s = int(input())
start = 1;
end = s

while start <= end:
    mid = (start + end) // 2
    if mid * (mid + 1) // 2 <= s:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
"""

# print(int(((int(input())*8+1)**.5-1)/2))