print("Enter details for 4 salesperson\n")
y = []
count = 0
for i in range(4):
    s = "Salesperson" + str(i+1) + ":\n"
    print(str)
    while(count < 5):
        x = list(map(int, raw_input("Enter:").split()))
        y.append(x)
        c = input("Continue>[y/n]")
        count += 1
        if c == 'n':
            break
count = 0
for i in y:
    i.count()
