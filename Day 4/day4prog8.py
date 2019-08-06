i = 0
total = 0
avg = 0
a = []
while 1:
    try:
        x = input("Enter:")
    except:
        continue
    if x == "done":
        break
    a.append(x)

i = 0
for i in a:
    print(i)
print("Exhausted")
