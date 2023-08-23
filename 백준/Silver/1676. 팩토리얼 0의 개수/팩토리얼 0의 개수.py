n=int(input())
cnt,result=0,1
for i in range(n,1,-1):
    result*=i
for i in str(result)[::-1]:
    if(i=='0'):
        cnt+=1
    else:
        break
print(cnt)