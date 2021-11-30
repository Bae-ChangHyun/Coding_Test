import sys
n=int(sys.stdin.readline())
for i in range(n):
    if(i!=n-1 and i!=0):
        print((n-1-i)*" "+"*"+(2*i-1)*" "+"*")
    else:
        print(" "*(n-1-i)+(2*i+1)*"*")