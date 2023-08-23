import sys
n=int(sys.stdin.readline())

for i in range(-n,n+1,1):
    if(i!=0 and i!=1):
        i=abs(i)
        print(" "*(n-i)+(i-1)*"*"+"*"+(i-1)*"*")