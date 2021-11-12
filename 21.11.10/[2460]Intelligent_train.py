result=0
people=0
for i in range(10):
    a,b=map(int,input().split())
    people+=b-a
    result=max(result,people)
print(result)