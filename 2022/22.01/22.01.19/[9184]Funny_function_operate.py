import sys
input=sys.stdin.readline

dp=[]
for i in range(101):
    dp.append([])
    for j in range(101):
        dp[i].append([])
        for k in range(101):
            dp[i][j].append([0])

dp[20][20][20]=1048576
for i in range(-50,51,1):
    for j in range(-50,51,1):
        for k in range(-50,51,1):
            if (i <= 0 or j <= 0 or k <= 0):
                dp[i][j][k]=1
            elif (i > 20 or j > 20 or k > 20):
                dp[i][j][k]=dp[20][20][20]
            elif (i < j and j < k):
                dp[i][j][k]=dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
            else:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1]
while(1):
    tmp=list(map(int,input().split()))
    if(tmp==[-1,-1,-1]):
        break
    else:
        print("w({0}, {1}, {2}) = {3}".format(tmp[0],tmp[1],tmp[2],dp[tmp[0]][tmp[1]][tmp[2]]))
        
