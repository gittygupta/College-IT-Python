d = {}
d2 = {}
for i in range(3):
    x = raw_input('Enter name:')
    y = raw_input('Enter class:')
    z = list(map(str, raw_input('Enter subjects:').split()))
    d['name'] = x
    d['class'] = y
    d['subject'] = z
    d2[i] = d
print(d2)
