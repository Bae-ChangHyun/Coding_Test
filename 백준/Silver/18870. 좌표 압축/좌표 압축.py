import sys
input =sys.stdin.readline 
n = int(input())
arr = list(map(int,input().split())) 
s = list(sorted(set(arr))) 
dic={value:index for index,value in enumerate(s)} 
for i in arr: 
	print(dic[i],end=" ")