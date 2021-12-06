import sys

a,b=map(int,sys.stdin.readline().split())
n=int(input())
num=0

word=list(map(int,sys.stdin.readline().split()))
word.reverse()

for idx,i in enumerate(word):
    num+=i*(a**idx)
word=[]
while(num!=0):
    r=num%b
    word.append(r)
    num//=b
for i in reversed(word):
    print(i,end="")
