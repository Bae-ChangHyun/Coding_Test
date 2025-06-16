import sys

n = int(sys.stdin.readline().strip())
stack = []

for i in range(n):
    temp = int(sys.stdin.readline().strip())
    if temp == 0: stack.pop()
    else:
        stack.append(temp)
print(sum(stack))