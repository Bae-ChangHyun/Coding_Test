import sys
input=sys.stdin.readline

while(1):
    code=input().rstrip()
    if(code=='END'):
        break
    print(code[::-1]) 