import sys
input = sys.stdin.readline

N=int(input())

print(int((N%4==0 and N%100!=0) or N%400==0))