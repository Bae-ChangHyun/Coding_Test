n = int(input())
L = set([i*i for i in range(1, 224)])
if n in L:
    print(1)
    exit()
for i in range(1, int(n**0.5)+1):
    if (n-i*i) in L:
        print(2)
        exit()
for i in range(1, int(n**(0.5)+1)):
    for j in range(1, int(n**0.5)+1):
        if (n-i*i-j*j) in L:
            print(3)
            exit()
print(4)