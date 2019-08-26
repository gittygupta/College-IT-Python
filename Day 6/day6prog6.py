n = input("Enter number of rows:")
def pascal(n):
    x = 1
    for i in range(0, n):
        print(x)
        x *= 11
pascal(n)
