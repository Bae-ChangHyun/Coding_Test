
#? 백준[1343]_폴리오미노_(그리디 연습문제)
#! [모범답안]
#a=input().replace('XXXX','AAAA').replace('XX','BB')
#print(-1 if'X'in a else a)

#! [내 답안]
board=input()
answer=[]

board_list=board.split('.')
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