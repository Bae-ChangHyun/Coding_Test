import sys
n=int(sys.stdin.readline())
tmp=[]

for _ in range(n):
    deck=[]
    deck=sys.stdin.readline().split()
    if(deck[0]=="push_front"):
        tmp=[int(deck[1])]+tmp
    elif(deck[0]=="push_back"):
        tmp.append(int(deck[1]))
    elif(deck[0]=="front"):
        if(tmp==[]):print(-1)
        else:print(tmp[0])
    elif(deck[0]=="back"):
        if(tmp==[]):print(-1)
        else:print(tmp[-1])
    elif(deck[0]=="size"):
        print(len(tmp))
    elif(deck[0]=="pop_front"):
        if(tmp==[]):print(-1)
        else:
            print(tmp[0])
            tmp=tmp[1:]
    elif(deck[0]=="pop_back"):
        if(tmp==[]):print(-1)
        else:
            print(tmp[-1])
            tmp=tmp[:-1]
    elif(deck[0]=="empty"):
        if(tmp):print(0)
        else:print(1)