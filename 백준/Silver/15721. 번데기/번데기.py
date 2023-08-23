import sys
input=sys.stdin.readline

a=int(input()) #총 인원수
t=int(input()) #번쨰
q=input().rstrip() #0=뻔/1=데기
cnt=0
command="01010011"

if(t>4):
    n=int(t/4+0.9)
    tmp=[0]*n
    command=""
    for i in range(0,n):
        tmp[i]="0101"+(i+2)*'0'+(i+2)*'1'
        command+=tmp[i]
for i in range(len(command)):
    if(command[i]==q):
        cnt+=1
    if(cnt==t):
        print(i%a)
        break