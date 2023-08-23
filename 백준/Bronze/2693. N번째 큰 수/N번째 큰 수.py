for i in range(int(input())):
    tmp=input().split()
    tmp=[int(i) for i in tmp]
    tmp.sort()
    print(tmp[-3])
    tmp=[]