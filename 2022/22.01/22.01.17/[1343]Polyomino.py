import sys
input=sys.stdin.readline

board=input().rstrip()

for i in range(len(board)):
    if(board[i]=='.'):
        continue
    elif(board[i:i+4]=='XXXX'):
        board=board[:i]+'AAAA'+board[i+4:]
    elif(board[i:i+2]=='XX'):
        board=board[:i]+'BB'+board[i+2:]
if('X' in board):
    print(-1)
else:
    print(board) 