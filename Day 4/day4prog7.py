i = 0
total = 0
avg = 0
x = input("Enter:")
maxi = x
mini = x
while 1:
    try:
        x = input("Enter:")
    except:
        continue
    if x == "done":
        break
    if x > maxi:
        maxi = x
    if x< mini:
        mini = x
    total += x
    i += 1
    avg = float(total / i)
    
print(total)
print(i)
print(avg)
print(maxi)
print(mini)
