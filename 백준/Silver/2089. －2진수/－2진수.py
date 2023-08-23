n=int(input())
tmp=""

while(n!=0):
    if(n%(-2)!=0):
        n=n//(-2)+1
        tmp+='1'
    else:
        n=n//(-2)
        tmp+='0'
if(tmp==""):
    tmp+='0'
print(tmp[::-1])