d = {}
x = list(map(str, raw_input('Enter keys:').split()))
y = list(map(str, raw_input('Enter values:').split()))
for i in range(len(x)):
	d[x[i]] = y[i]
for i in d.items():
    print i

