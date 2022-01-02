'''
k=int(input())
array=input().split()
array=[int(i) for i in array]
print(min(array),max(array))
'''
print(min(s:=[*map(int,[*open(0)][1].split())]),max(s))