d = {}
x = list(map(int, raw_input('Enter keys:').split()))
y = list(map(int, raw_input('Enter values:').split()))
z = int(raw_input('item to search:'))
for i in range(len(x)):
	d[x[i]] = y[i]
if z in d:
	print('Found')
