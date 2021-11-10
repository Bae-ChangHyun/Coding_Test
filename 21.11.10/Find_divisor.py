'''
divisor=[]
N,k=input().split()
N=int(N)
k=int(k)

for i in range(1,N+1):
    if(N%i==0):
        divisor.append(i)
if(len(divisor)<k):
    print(0)
else:
    print(divisor[k-1])
'''
N,K=map(int,input().split())
divisor=[i for i in range(1,N+1) if(N%i==0)]
if(len(divisor)<k):
    print(0)
else:
    print(divisor[k-1])

