'''
import sys
n=int(sys.stdin.readline())
tmp=sys.stdin.readline()
a=[]

for i in range(n):
    a.append(int(tmp[i]))
print(sum(a))
'''
input()
print(sum(map(int,input())))