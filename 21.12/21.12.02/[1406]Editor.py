word,n=input(),int(input())
loc=len(word)

for i in range(n):
    tmp=input().split()
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
print(word)