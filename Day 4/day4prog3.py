for i in range(1, 1000):
    total = 0
    z = str(i)
    length = len(z)
    for x in z:
        total += int(x) ** length
    if total == i:
        print(i)
