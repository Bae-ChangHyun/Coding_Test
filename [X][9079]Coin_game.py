import sys
input=sys.stdin.readline

n=int(input())
board=[]


for i in range(n):
    # 게임판 만들기
    for j in range(3):
        board.append(list(input().split()))
        while(1):
            if('H' not in board[j] and 'T' not in board[j]):
                break
            board[j].replace('H',0)
            board[j].replace('T',1)
        print(board)
            
    