N,k=input().split()
N=int(N)
k=int(k)

divisor=[i for i in range(1,N+1) if(N%i==0)]
if(len(divisor)<k):
    print(0)
else:
    print(divisor[k-1])