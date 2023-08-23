a=b=1
for i in range(int(input())):
	a,b=b,2*a+b
print(a%10007)