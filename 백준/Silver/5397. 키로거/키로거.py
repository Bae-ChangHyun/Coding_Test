from collections import deque
T = int(input())
for _ in range(T):
    L = input()
    left = deque()
    right = deque()
    for i in L:
        if(i=="<"):
            if(len(left)!=0):
                right.appendleft(left.pop())
        elif(i==">"):
            if(len(right)!=0):
                left.append(right.popleft())
        elif(i=="-"):
            if(len(left)!=0):
                left.pop()
        else:
            left.append(i)
    print(''.join(left+right))