import calendar
x = input('Enter year:')
m = calendar.month_name
for i in range(1, 13):
    j = calendar.monthcalendar(x, i)
    if j[0][0] != 0:
        break
print m[i]
