d = {}
x = list(map(int, raw_input('Enter keys:').split()))
y = list(map(int, raw_input('Enter values:').split()))
d = dict(zip(x, y))
d2 = dict(zip(d.values(), d.keys()))
print(d2)
