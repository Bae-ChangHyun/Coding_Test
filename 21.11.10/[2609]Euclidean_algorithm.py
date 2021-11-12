'''
a,b=input().split()
a=int(a)
b=int(b)

lcm,gcd=1,a*b

while(lcm!=0):
    lcm=a%b
    a,b=b,lcm
print(a)
print(int(gcd/a))
'''
a,b=map(int,input().split())
L=a*b
while b:
    a,b=b,a%b
print(a,L//a)
    