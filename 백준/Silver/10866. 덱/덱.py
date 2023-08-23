import sys
n=int(sys.stdin.readline())
tmp=[]

for _ in range(n):
    que=[]
    que=sys.stdin.readline().split()
    if(que[0]=="push_front"):
        tmp=[int(que[1])]+tmp
    elif(que[0]=="push_back"):
        tmp.append(int(que[1]))
    elif(que[0]=="front"):
        if(tmp==[]):print(-1)
        else:print(tmp[0])
    elif(que[0]=="back"):
        if(tmp==[]):print(-1)
        else:print(tmp[-1])
    elif(que[0]=="size"):
        print(len(tmp))
    elif(que[0]=="pop_front"):
        if(tmp==[]):print(-1)
        else:
            print(tmp[0])
            tmp=tmp[1:]
    elif(que[0]=="pop_back"):
        if(tmp==[]):print(-1)
        else:
            print(tmp[-1])
            tmp=tmp[:-1]
    elif(que[0]=="empty"):
        if(tmp):print(0)
        else:print(1)