import sys
n=int(sys.stdin.readline())
tmp=[]

for i in range(n):
    tmp.append(sys.stdin.readline().rstrip().split())
tmp=sorted(tmp,key=lambda x:int(x[0]))

for i in tmp:
    print(i[0],i[1])