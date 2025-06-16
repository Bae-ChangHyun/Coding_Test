import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    stack = []
    temp = sys.stdin.readline().strip()
    for j in range(len(temp)):
        if len(stack)>0:
            last = stack[-1]
            if temp[j] == ")" and last == "(":
                stack.pop()
            else:
                stack.append(temp[j])
        else:
            stack.append(temp[j])
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")