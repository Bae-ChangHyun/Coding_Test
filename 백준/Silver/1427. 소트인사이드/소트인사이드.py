import sys
input = sys.stdin.readline

array = input().rstrip()
n_array = [i for i in array]
n_array.sort(reverse=True)
print(int("".join(n_array)))
