n = input("Enter a number:")
flag = 0
for i in range(2, n):
    if(n%i == 0):
        print("Not prime")
        flag += 1
        break
if flag is not 1:
    print("Prime")
