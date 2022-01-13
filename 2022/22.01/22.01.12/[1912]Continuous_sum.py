input()
a=m=-1e9
for x in input().split():
    a=max(0,a)+int(x)
    m=max(m,a)
    print(m)
print(m)