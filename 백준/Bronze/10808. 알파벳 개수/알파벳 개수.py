from collections import Counter
import sys
from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
tmp=sys.stdin.readline().rstrip()
for i in alphabet_list:
    if(i in Counter(tmp)):
        print(Counter(tmp)[i],end=" ")
    else:
        print(0,end=" ")
