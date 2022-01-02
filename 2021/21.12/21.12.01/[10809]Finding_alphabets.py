from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
s=input()

for i in alphabet_list:
    if(i in s):
        print(s.find(i),end=" ")
    else:
        print(-1,end=" ")