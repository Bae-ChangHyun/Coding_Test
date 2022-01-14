import sys
input=sys.stdin.readline

command=list(input().split())

for i in command:
    flag=0
    if(i==command[0]):
        continue
    i=i[:-1]
    for j in range(len(i)):
        if(i[j].isalpha()==1):
            for k in range(j+1,len(i)):
                if(i[k].isalpha()==0):
                    flag=1
                    break
            if(flag==1):
                tmp=i[k:][::-1]+" "+i[j:k]+';'
            else:
                tmp=" "+i[j:]+';'
            tmp=tmp.replace('][','[]')
            print(command[0]+tmp)
            break