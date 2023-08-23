import sys

input=sys.stdin.readline

forest=dict()

while True:
    tree=input().rstrip('\n')
    if(not tree):break
    if(tree in forest):
        forest[tree]+=1
    else:
        forest[tree]=1
total=float(sum(forest.values()))

#forest2=sorted(forest,key=lambda x:x[0])
forest2=list(forest.keys())
forest2=sorted(forest2)
#print(forest2)

for i in forest2:
    print("%s %.4f"%(i,forest[i]/total*100))

