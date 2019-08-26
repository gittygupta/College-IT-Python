def fact(x):
    pro = 1
    for i in range(1, x+1):
        pro *= i
    return pro

def perm(n, r):
    return (fact(n)/(fact(n - r) * fact(r)))

n = input("n = ")
r = input("r = ")
print(perm(n, r))
