h,w=map(int,input().split())
if(h==1 or w==1):
    answer=1
elif(h<3):
    answer=(w-1)//2+1
else:
    answer=w
if(answer>=5):
    if(h>=3):answer=max(4,5+(w-7))
    else:answer=4
print(answer)
    