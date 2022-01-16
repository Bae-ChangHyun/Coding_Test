import sys
input=sys.stdin.readline

current=input()
throw=input()

if(current==throw):
    print("24:00:00")
else:
    current=int(current[0:2])*3600+int(current[3:5])*60+int(current[6:8])
    throw=int(throw[0:2])*3600+int(throw[3:5])*60+int(throw[6:8])
    if(current>throw):
        throw+=24*3600
    time=throw-current
    print("%02d:%02d:%02d"%(time//3600,time%3600//60,time%3600%60))