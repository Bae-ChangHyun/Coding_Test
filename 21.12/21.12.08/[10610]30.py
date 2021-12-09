n,res=list(map(int,[i for i in input()])),-1
tmp=""

if(sum(n)%3!=0 or (0 not in n)):
    print(-1)
else:
    n=sorted(n,reverse=True)
    for i in n:
        tmp+=str(i)
    print(int(tmp))
    
"""
n=int("".join(sorted(input())[::-1]))
print(n if n%30==0else-1) 
"""