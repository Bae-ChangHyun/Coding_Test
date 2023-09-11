import sys
input=sys.stdin.readline

n = int(input())
card=list(map(int,input().split()))
card.sort()
m=int(input())
array=list(map(int,input().split()))

def binary_search(target,start,end):
    if(start>end):
        print(0,end=' ')
        return 
    mid=(start+end)//2
    if(card[mid]==target):
        print(1,end=' ')
    elif(card[mid]<target):
        binary_search(target,mid+1,end)
    elif(card[mid]>target):
        binary_search(target,start,mid-1)
    
for i in array:
    binary_search(i,0,len(card)-1)