d = {}
x = list(map(int, raw_input('Enter keys:').split()))
y = list(map(int, raw_input('Enter values:').split()))
for i in range(len(x)):
	d[x[i]] = y[i]
for i in d.items():
    print i
