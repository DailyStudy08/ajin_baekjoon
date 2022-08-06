import sys
import datetime
y,m,d = map(int,(sys.stdin.readline().split()))
Y,M,D = map(int,(sys.stdin.readline().split()))

today_data = datetime.datetime(y,m,d)
dday_data = datetime.datetime(Y,M,D)
dday = dday_data - today_data

if dday_data >= datetime.datetime(y+1000,m,d):
    print('gg')
else:
    print(f'D-{dday.days}')
