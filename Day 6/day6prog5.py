n = input("Enter number:")
def fib(n):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

def fibrec(n):
    if n <= 1:
        return n
    return fibrec(n-1) + fibrec(n-2)

for i in range(0, n):
    print(fibrec(i))
