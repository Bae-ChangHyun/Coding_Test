import sys
tmp=sys.stdin.readline()
start=0
for i in range(len(tmp)):
    if(i%10==9 or i==len(tmp)-1):
        print(tmp[start:i+1])
        start=i+1
"""
s=input()
while s:
    print(s[:10])
    s=s[10:]
"""