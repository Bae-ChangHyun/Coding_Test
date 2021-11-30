import sys
n=int(sys.stdin.readline())
tmp=[]

for _ in range(n):
    board=[]
    board=sys.stdin.readline().split()
    if(board[0]=="push"):
        tmp.append(int(board[1]))
    elif(board[0]=="top"):
        if(tmp==[]):
            print(-1)
        else:print(tmp[-1])
    elif(board[0]=="size"):
        print(len(tmp))
    elif(board[0]=="pop"):
        if(tmp==[]):
            print(-1)
        else:
            print(tmp[-1])
            tmp=tmp[:-1]
    elif(board[0]=="empty"):
        if(tmp):
            print(0)
        else:
            print(1)