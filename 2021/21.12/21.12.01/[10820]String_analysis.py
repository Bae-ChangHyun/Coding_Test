import sys
result=[0]*4

while(1):
    try:
        tmp=sys.stdin.readline().rstrip('/n')
        if(tmp=""):
            break
        for i in tmp:
            if('a'<=i<='z'):
                result[0]+=1
            elif('A'<=i<='Z'):
                result[1]+=1
            elif(i.isdigit()==1):
                result[2]+=1
            elif(i==" "):
                result[3]+=1
        print(result[0],result[1],result[2],result[3])
        result=[0]*4
    except EOFError:
        break
        
"""
while 1:
 try:x=input();a=b=c=d=0
 except:break
 for i in x:
  if ord(i)<33:d+=1
  elif 96<ord(i)<123:a+=1
  elif 64<ord(i)<91:b+=1
  else:c+=1
 print(a,b,c,d)
"""