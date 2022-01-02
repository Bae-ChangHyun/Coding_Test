import sys

a,b=map(int,sys.stdin.readline().split())
if(b>a): a,b=b,a
while(b!=0):
    a=a%b
    a,b=b,a
print(a*'1')