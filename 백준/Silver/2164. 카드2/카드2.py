import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
stack=deque([i+1 for i in range(n)])

while(len(stack)!=1):
    stack.popleft()
    a=stack[0]
    stack.popleft()
    stack.append(a)
print(*stack)
