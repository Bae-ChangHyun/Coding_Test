import sys

n=int(sys.stdin.readline())
for i in range(n):
    print("*"*(i+1)+" "*(n-1-i)*2+"*"*(i+1))
for i in range(n-1,0,-1):
    print("*"*i+" "*(n-i)*2+"*"*i)
    
    
"""
a = int(input())
for i in range(-a+1,a):
    i=abs(i)
    print('*'*(a-i)+' '*(2*i)+'*'*(a-i))
"""
    