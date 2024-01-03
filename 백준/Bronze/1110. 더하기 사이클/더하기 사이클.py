import sys
import math
input=sys.stdin.readline

N=int(input())
init=N
cnt=0
while(1):
    tmp=N//10+N%10
    N=N%10*10+tmp%10
    cnt+=1
    if(N==init):
        print(cnt)
        break