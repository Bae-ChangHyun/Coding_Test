import sys

n=int(sys.stdin.readline())
board=dict()
for i in range(n):
    tmp=int(sys.stdin.readline())
    if(tmp not in board):
        board[tmp]=1
    else:
        board[tmp]+=1
board=sorted(board.items(),key=lambda x:(-x[1],x[0]))
print(board)