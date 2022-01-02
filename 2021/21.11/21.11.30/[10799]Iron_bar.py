"""
sums=0
tmp=input()
tmp=[i for i in tmp]
for i in range(len(tmp)):
    if(tmp[i]==')'):
        for j in range(i-1,-1,-1):
            if(tmp[j]=='('):
                if(j==i-1):
                    tmp[i]='L'
                    tmp[j]='L' #레이저부분을 저장해두면서 총길이 안바꾸려고 ()를 LL로 바꿔둠
                    break
                sums+=(tmp[j:i+1].count('L')//2)+1   #부셔진 조각의 수는 기둥사이에 있는 레이저개수 +1
                tmp[j]='D' #이미 체크한 기둥의 (부분만 d로바꿔서 체킹해줌 
                break
#print(tmp)
print(sums)
"""
arr = list(input())
bar = 0 #현재 짝대기 개수
cnt = 0 # 정답 
i = 0
while 1:
    if i==len(arr)-1: break
    if arr[i]=='(':
        if arr[i+1]==')':
            cnt+=bar
            i+=2
            continue
        bar+=1
        cnt+=1
    else:
        bar-=1
    i+=1
print(cnt)

