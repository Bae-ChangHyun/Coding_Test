origin=input()
tmp=['0']*len(origin)
for i in range(len(origin)):
    tmp[i]=origin[i:]
tmp.sort()
for i in tmp:
    print(i)