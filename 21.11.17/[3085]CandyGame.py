import copy             # copy 모듈을 가져옴

n=int(input())
board,sums = [],[]

for i in range(n):
    tmp=input()
    tmp=[i for i in tmp]
    board.append(tmp)    
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
board = list(map(list, zip(*board)))
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
#우선 옆으로 바꾸는 것부터 해보자
tmp=copy.deepcopy(board)
for i in range(n):
    for j in range(n-1):
        if(tmp[i][j]!=tmp[i][j+1]):
            tmp[i][j],tmp[i][j+1]=tmp[i][j+1],tmp[i][j]
            coltmp=[k[j] for k in tmp]
            cnt=1
            for k in range(len(coltmp)-1):
                if(coltmp[k]==coltmp[k+1]):
                    cnt+=1
                else:
                    sums.append(cnt)
                    cnt=1
            if(cnt!=1):
                sums.append(cnt)
                cnt=1
            #print(coltmp,"and",sums)
            coltmp=[k[j+1] for k in tmp]
            for k in range(len(coltmp)-1):
                if(coltmp[k]==coltmp[k+1]):
                    cnt+=1
                else:
                    sums.append(cnt)
                    cnt=1
            if(cnt!=1):
                sums.append(cnt)
                cnt=1
            #print(coltmp,"and",sums)
            tmp=copy.deepcopy(board)   
# 이제 아래로 바꾸는 걸 해보자(위와 코드 동일하고 리스트만 전치시킴)
board = list(map(list, zip(*board)))
tmp=copy.deepcopy(board)
for i in range(n):
    for j in range(n-1):
        if(tmp[i][j]!=tmp[i][j+1]):
            tmp[i][j],tmp[i][j+1]=tmp[i][j+1],tmp[i][j]
            coltmp=[k[j] for k in tmp]
            cnt=1
            for k in range(len(coltmp)-1):
                if(coltmp[k]==coltmp[k+1]):
                    cnt+=1
                else:
                    sums.append(cnt)
                    cnt=1
            if(cnt!=1):
                sums.append(cnt)
                cnt=1
            #print(coltmp,"and",sums)
            coltmp=[k[j+1] for k in tmp]
            for k in range(len(coltmp)-1):
                if(coltmp[k]==coltmp[k+1]):
                    cnt+=1
                else:
                    sums.append(cnt)
                    cnt=1
            if(cnt!=1):
                sums.append(cnt)
                cnt=1
            #print(coltmp,"and",sums)
            tmp=copy.deepcopy(board) 
print(max(sums))
                        
            








