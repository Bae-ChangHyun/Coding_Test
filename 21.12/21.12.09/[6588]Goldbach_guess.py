import sys

check = [0, 0] + [1] * 1000000
for i in range(2, 1001):
    if check[i] == True:
        for j in range(i + i, 1000001, i):
            check[j] = False
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    A = 0
    B = n
    for _ in range(1000000):
        if check[A] and check[B]:
            print(f"{n} = {A} + {B}")
            break
        A += 1
        B -= 1
    else:
        print("Goldbach's conjecture is wrong.")