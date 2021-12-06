import sys

a,b=map(int,sys.stdin.readline().split())
n=int(input())
num=0

word=list(map(int,sys.stdin.readline().split()))
word.reverse()
#17진법으로 나타낸 숫자의 자리수의 갯수가 2
#17진법을 이루고 있는 숫자 2개가 공백을 구분으로 높은 자리부터 차례대로 주어진다.
16*1+17*2


for idx,i in enumerate(word):
    num+=(idx+1)*i*a
print(num)
