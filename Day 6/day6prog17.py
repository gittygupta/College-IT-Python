def leap(y):
    if y%400 == 0 or y%4 == 0 and y%100 != 0:
        print("Leap")
    else:
        print("Not leap")

year = input("Year:")
leap(year)
