import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    rom=[]
    pos=[0,0]
    nav=[1,0,0,0]
    mxposx,mnposx,mxposy,mnposy=0,0,0,0
    command=input()
    for j in command:
        if(nav[0]==1):
            if(j=='F'):
                pos[1]+=1
            elif(j=='B'):
                pos[1]-=1
            elif(j=='L'):
                nav[0],nav[2]=0,1
            elif(j=='R'):
                nav[0],nav[3]=0,1
        elif(nav[1]==1):
            if(j=='F'):
                pos[1]-=1
            elif(j=='B'):
                pos[1]+=1
            elif(j=='L'):
                nav[1],nav[3]=0,1
            elif(j=='R'):
                nav[1],nav[2]=0,1
        elif(nav[2]==1):
            if(j=='F'):
                pos[0]-=1
            elif(j=='B'):
                pos[0]+=1
            elif(j=='L'):
                nav[2],nav[1]=0,1
            elif(j=='R'):
                nav[2],nav[0]=0,1
        else:
            if(j=='F'):
                pos[0]+=1
            elif(j=='B'):
                pos[0]-=1
            elif(j=='L'):
                nav[3],nav[0]=0,1
            elif(j=='R'):
                nav[3],nav[1]=0,1
        mxposx=max(mxposx,pos[0])
        mnposx=min(mnposx,pos[0])
        mxposy=max(mxposy,pos[1])
        mnposy=min(mnposy,pos[1])
    result=(mxposx-mnposx)*(mxposy-mnposy)
    print(result)
        
