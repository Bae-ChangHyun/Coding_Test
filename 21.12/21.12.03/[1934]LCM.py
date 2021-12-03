import sys
n=int(input())

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    c=a*b
    while(b!=0):
        if(b>a): a,b=b,a
        a=a%b
        a,b=b,a
    print(c//a)

"""
import math
for _ in[0]*int(input()):
    print(math.lcm(*map(int,input().split())))
"""