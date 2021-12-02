"""
import sys
word,n=input(),int(input())
loc=len(word)

for i in range(n):
    tmp=sys.stdin.readline().rstrip().split()
    if(tmp[0]=='L'):
        if(loc!=0):loc-=1
    elif(tmp[0]=='D'):
        if(loc!=len(word)):loc+=1
    elif(tmp[0]=='B'):
        if(loc!=0):
            word=word[:loc-1]+word[loc:]
            loc-=1
    else:
        word=word[:loc]+tmp[1]+word[loc:]
        loc+=1
print(word)
"""
from sys import stdin
 
stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
    if line[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif line[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue
    elif line[0] == 'B':
        if stk1: stk1.pop()
        else: continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))