import datetime
x = list(map(int, raw_input().split('/')))
print(datetime.datetime(x[2], x[1], x[0]))
