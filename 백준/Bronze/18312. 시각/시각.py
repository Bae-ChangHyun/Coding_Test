import sys
input=sys.stdin.readline

n,t=input().split()
cnt=0

for i in range(int(n)+1):
    if(i<10):tmp='0'+str(i)
    else:tmp=str(i)
    if(t in tmp):
        cnt+=3600
        continue
    for j in range(60):
        if(j<10):tmp1='0'+str(j)
        else:tmp1=str(j)
        if(t in tmp1):
            cnt+=60
            continue
        for k in range(60):
           if(k<10):tmp2='0'+str(k)
           else:tmp2=str(k)
           if(t in tmp2):
                cnt+=1
print(cnt)