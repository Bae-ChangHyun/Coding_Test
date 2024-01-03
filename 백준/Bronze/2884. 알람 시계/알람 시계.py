import sys
input=sys.stdin.readline

h,m = map(int,input().split())

if(m<45):
    h-=1
    m+=15
    if(h<0):h+=24
else:
    m-=45
print(h,m)