import datetime

a,b,c,d,e = map(int, input().split())

t1 = datetime.datetime(year=2020, month=1, day=1, hour=a, minute=b)
t2 = datetime.datetime(year=2020, month=1, day=1, hour=c, minute=d)

delta = t2 - t1
m = int(delta.seconds / 60)
print(m - e)