s=input()
for i in range(len(s)):
    if(s[i].isalpha()==1):
        tmp=ord(s[i])+13
        if('a'<=s[i]<='z'):
            if(tmp>122): tmp-=26
            s=s[:i]+chr(tmp)+s[i+1:]
        else:
            if(tmp>90): tmp-=26
            s=s[:i]+chr(tmp)+s[i+1:]
            
print(s)
"""
import codecs
print(codecs.encode(input(),"rot13"))
"""
"""
def f(c):
    i=ord(c)
    if i>96:return chr((i-84)%26+97)
    if i>64:return chr((i-52)%26+65)
    return c
print(''.join(map(f,input())))
"""