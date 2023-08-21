people=list(map(int,input().split()))
limit=int(input())

people.sort()
answer=0

while(1):
    if(len(people)<=1):
        #answer+=1
        break
    tmp=people[0]+people[-1]
    if(tmp>limit):
        people.pop(-1)
    else:
        people.pop(0)
        people.pop(-1)
    answer+=1
print(answer) 