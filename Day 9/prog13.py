import datetime
y = datetime.date.today().strftime("%Y")
d = datetime.date.today().strftime("%d")
t = datetime.datetime.now()
t = str(t)
m = t[5:7]
t = t[12:20]
print('year : ' + str(y))
print('month : ' + str(m))
print('day : ' + str(d))
print('time : ' + str(t))
print('date and time : ' + str(m) + '/' + str(d) + '/' + str(y) + ', ' + str(t))
