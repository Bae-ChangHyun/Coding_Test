import sys
n=int(sys.stdin.readline())
check=[]

for i in range(n):
    tmp=sys.stdin.readline().rstrip()
    tmp=[i for i in tmp]
    for j in tmp:
        if(check==[]):
            check.append(j)
        else:
            if(check[-1]=="(" and j==")"):
                check=check[:-1]
            else:
                check.append(j)
    if(check==[]):
            print("YES")
    else:
            print("NO")
    check=[]

"""
for _ in range(int(input())):
    s=input()
    while '()' in s:
        s=s.replace('()','')
    print('NO'if s else'YES')
"""