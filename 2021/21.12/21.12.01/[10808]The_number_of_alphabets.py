from collections import Counter
from string import ascii_lowercase
import sys

alphabet_list = list(ascii_lowercase)

tmp=sys.stdin.readline().rstrip()

for i in alphabet_list:
    if(i in Counter(tmp)):
        print(Counter(tmp)[i],end=" ")
    else:
        print(0,end=" ")

#print(*map(input().count,map(chr,range(97,123))))