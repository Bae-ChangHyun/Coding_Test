import sys

n=int(sys.stdin.readline())
for i in range(n):
    print((n-i-1)*" "+"*"*(i+1))
for i in range(n-1):
    print((i+1)*" "+(n-i-1)*"*")

"""
for i in range(1,2*n):
    print(' '*(abs(n-i))+'*'*(n-abs(-i+n)))
"""