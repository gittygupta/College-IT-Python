d = {}
x = list(map(int, raw_input('Enter keys:').split()))
y = list(map(int, raw_input('Enter values:').split()))
d = dict(zip(x, y))
p = 0
for i in d.values():
    p += i
print p
