import random
from itertools import permutations

n=int(input())
answer,tanswer,limit=0,0,1
tmp=list(map(int,input().split()))

for i in permutations(tmp,n):
    for j in range(len(i)):
        if(j!=len(i)-1):
            tanswer+=abs(i[j]-i[j+1])
    answer=max(tanswer,answer)
    tanswer=0
print(answer)

# tmp2=[]
# for i in range(1,n+1,1):
#     limit*=i
# #while(1):
# for i in range(10):
#     random.shuffle(tmp)
#     if tmp not in tmp2:
#         tmp2.append(tmp)
#         print(tmp2, tmp)
#     else:
#         print("같음")
#     for i in range(len(tmp)):
#         if(i!=len(tmp)-1):
#             tanswer+=abs(tmp[i]-tmp[i+1])
#     answer=max(tanswer,answer)
#     tanswer=0
#     #print(tmp2)
#     if(len(tmp2)==limit):
#         break
# print(answer)


    
    


