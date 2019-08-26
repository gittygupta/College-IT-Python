x = input("Enter number:")
def factors(x):
    for i in range(1, (x/2 + 1)):
        if x%i == 0:
            print(i)

factors(x)
