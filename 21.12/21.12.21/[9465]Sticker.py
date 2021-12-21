import sys

t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    sticker,dp=[],[] #sticker은 남은스티커, dp는 고른스티커
    sticker.append(list(map(int,sys.stdin.readline().split())))
    sticker.append(list(map(int,sys.stdin.readline().split())))
    # print(sticker)
    while(sum(sticker[0])+sum(sticker[1])!=(-2*n)): #스티커를 모두 뗐으면 종료
        tmp=max(max(sticker[0]),max(sticker[1])) #이러면 tmp가 가장 큰수로 정해짐 우선 
        if(tmp in sticker[0]):row=0
        else:row=1
        dp.append(tmp)
        row=sticker.index(sticker[row]) 
        col=sticker[row].index(tmp)
        sticker[row][col]=-1
        #인접합 스티커도 떼는 과정 
        if(col==0):sticker[row][col+1]=-1
        elif(col==n-1):sticker[row][col-1]=-1
        else:
            sticker[row][col-1]=-1
            sticker[row][col+1]=-1
        if(row==0):sticker[row+1][col]=-1
        else:sticker[row-1][col]=-1
        #print(sticker)
    #print(dp)
    print(sum(dp))
    dp=[]
        
      