import random
d = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(6000):
    x = random.randint(1, 6)
    if x == 1:
        d[1] += 1
    if x == 2:
        d[2] += 1
    if x == 3:
        d[3] += 1
    if x == 4:
        d[4] += 1
    if x == 5:
        d[5] += 1
    if x == 6:
        d[6] += 1
for i in d.items():
    print(i)
