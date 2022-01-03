import sys
input=sys.stdin.readline

command=list(input().split())
print(command)

for i in command:
    if(i==command[0]):
        continue
    i=i[:-1]
    for j in range(len(i)):
        if(i[j].isalpha()==1):
            tmp=i[j+1:][::-1]
            print(tmp)
            i=tmp+i[:j+1]
            print(i)
            break
            
            
print(command)