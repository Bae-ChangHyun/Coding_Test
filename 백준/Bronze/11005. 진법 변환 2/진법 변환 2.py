import sys
import string

tmp=list(map(int,sys.stdin.readline().split()))
upper=[j for j in string.ascii_uppercase]
table,result=dict(),""

for i in range(10,36):
    table[i]=upper[i-10]
while(tmp[0]!=0):
    a=tmp[0]%tmp[1]
    tmp[0]=tmp[0]//tmp[1]
    if(a>=10):
        result+=table[a]
    else:
        result+=str(a)
print(result[::-1])
    
    