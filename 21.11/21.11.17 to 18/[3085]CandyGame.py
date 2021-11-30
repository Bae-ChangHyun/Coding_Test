def init(board,n,sums):
    cnt=1
    for i in range(n):
        for j in range(n-1):
            if(board[i][j]==board[i][j+1]):
                cnt+=1
            else:
                sums.append(cnt)
                cnt=1
        if(cnt!=1):
            sums.append(cnt)
            cnt=1
    return sums
    
def calc(board,n,sums):
    tmp=copy.deepcopy(board)
    for i in range(n):
        for j in range(n-1):
            if(tmp[i][j]!=tmp[i][j+1]):
                tmp[i][j],tmp[i][j+1]=tmp[i][j+1],tmp[i][j]
                coltmp=[k[j] for k in tmp]
                sums=main(coltmp,n,sums)
                coltmp=[k[j+1] for k in tmp]
                sums=main(coltmp,n,sums)
                coltmp=tmp[i]
                sums=main(coltmp,n,sums)
                tmp=copy.deepcopy(board)

def main(arr,n,sums):
    cnt=1
    for i in range(n-1):
        if(arr[i]==arr[i+1]):
            cnt+=1
        else:
            sums.append(cnt)
            cnt=1
    if(cnt!=1):
        sums.append(cnt)
        cnt=1
    return sums

import copy             # copy 모듈을 가져옴

n=int(input())
board,sums = [],[]
# 필수부분:board를 이중리스트로 만듦
for i in range(n):
    tmp=input()
    tmp=[i for i in tmp]
    board.append(tmp)    
# 처음옮기기 전 최대먹을 수 있는 사탕개수를 세기    
init(board,n,sums)        
board = list(map(list, zip(*board)))
init(board,n,sums)
calc(board,n,sums) #같은 행에 있는 것끼리 바꾸기(좌우)  
board = list(map(list, zip(*board))) #board 전치
calc(board,n,sums) #같은 행에 있는 것끼리 바꾸기(상하)
print(max(sums))