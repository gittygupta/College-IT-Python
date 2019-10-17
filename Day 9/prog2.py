import calculator as c
x = list(raw_input('Enter the operation with spaces:').split())
if x[1] == '+':
    print('Result = ' + str(c.add(int(x[0]), int(x[2]))))
if x[1] == '-':
    print('Result = ' + str(c.sub(int(x[0]), int(x[2]))))
if x[1] == '*':
    print('Result = ' + str(c.mul(int(x[0]), int(x[2]))))
if x[1] == '/':
    print('Result = ' + str(c.div(int(x[0]), int(x[2]))))
if x[1] == '^':
    print('Result = ' + str(c.exp(int(x[0]), int(x[2]))))
    
