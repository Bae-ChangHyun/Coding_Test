n,start,end=map(int, input().split())
cnt=0
while start!=end:
  start -= start//2
  end -= end//2
  cnt+=1
print(cnt)