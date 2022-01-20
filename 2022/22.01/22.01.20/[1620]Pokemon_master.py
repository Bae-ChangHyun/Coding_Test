import sys
input=lambda:sys.stdin.readline().strip()
dic={}
a,b=map(int,input().split())
for i in range(a):
    s=input()
    dic[s]=str(i+1)
    dic[str(i+1)]=s
for i in range(b):
    print(dic[input()])

"""
import sys
input=sys.stdin.readline

dogam_n=dict()
dogam_w=dict()
n,m=map(int,input().split())
for i in range(n):
    name=input().rstrip()
    dogam_n[i+1]=name
    dogam_w[name]=i+1
for i in range(m):
    q=input().rstrip()
    if(q[0].isalpha()):
        print(dogam_w[q])
    else:
        print(dogam_n[int(q)])
"""