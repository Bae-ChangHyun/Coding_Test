a=b=1
for i in range(int(input())):
	a,b=b,a+b
print(a%10007)