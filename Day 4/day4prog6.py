i = 0
total = 0
avg = 0
while 1:
    try:
        x = input("Enter:")
    except:
        continue
    if x == "done":
        break
    total += x
    i += 1
    avg = float(total / i)
    
print(total)
print(i)
print(avg)
