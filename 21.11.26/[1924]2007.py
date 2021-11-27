info={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
day={0:'MON',1:'TUE',2:'WED',3:'THU',4:"FRI",5:"SAT",6:'SUN'}
month=[i for i in info.keys()]
m,y=map(int,input().split())
print(month[0:m],y-1)
tmp=[info[i] for i in month[0:m-1]]
print(day[(sum(tmp)+y-1)%7])
