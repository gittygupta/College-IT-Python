import calendar
x = list(raw_input('Enter Range:').split())
tot = 0
print('Leap Years in range:')
for i in range(int(x[0]), int(x[1])):
    if calendar.isleap(i):
        tot += 1
print(tot)
