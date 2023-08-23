charge=int(input())

answer=0
for i in range(charge//5,0,-1):
    if((charge-(5*i))%2==0):
        answer=i+(charge-(5*i))//2
        break
if(answer==0):
    if(charge%2==0):answer=charge//2
    else:answer=-1

print(answer)
    