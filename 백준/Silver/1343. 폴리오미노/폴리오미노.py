board=input()
answer=[]

board_list=board.split('.')
#print(board_list)
for i in board_list:
    if(len(i)%2==1):
        answer=['-1','.']
        break
    else:
        if(len(i)%4==0):
            answer.append('A'*len(i))
        elif(len(i)%4>1):
            answer.append('A'*(len(i)//4*4))
            answer.append('B'*(len(i)%4))
        else:
            answer.append('B'*len(i))
    answer.append('.')
answer=''.join(answer)
print(answer[:-1])