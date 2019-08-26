def fact(x):
    pro = 1
    for i in range(1, x+1):
        pro *= i
    return pro
def series(n):
    summ = 0.0
    for i in range(1, n+1):
        summ += float((i ** i) / fact(i))
    return summ

n = input("Enter n:")
print(series(n))
