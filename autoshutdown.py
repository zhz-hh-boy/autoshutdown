import time
import os
import csv
shut_time=[]
f=open('shut_time_list.csv','r')
shut_time=list(csv.reader(f))
for i in range(len(shut_time)):
    for j in range(len(shut_time[i])):
        shut_time[i][j]=int(shut_time[i][j])
f.close()
while True:
    time_now=time.localtime(time.time())
    time_day=time.strftime("%w",time_now)
    time_hour=time.strftime("%H",time_now)
    time_minute=time.strftime("%M",time_now)
    time_day=int(time_day)
    time_hour=int(time_hour)
    time_minute=int(time_minute)
    if (time_hour==shut_time[0][time_day] and time_minute==shut_time[1][time_day]):
        os.system("shutdown /p")
        break
    else:
        time.sleep(1)