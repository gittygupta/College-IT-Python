def fact(x):
    pro = 1
    for i in range(1, x+1):
        pro *= i
    return pro

def comb(n, r):
    return (fact(n)/fact(n - r))

n = input("n = ")
r = input("r = ")
print(comb(n, r))
