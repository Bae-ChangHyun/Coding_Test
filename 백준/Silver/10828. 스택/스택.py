import sys

n = int(sys.stdin.readline().strip())
stack = []

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    try: order, num = temp.split(" ")
    except: order = temp
    
    if order == "push":
        stack.append(num)
    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        print(1 if not stack else 0)