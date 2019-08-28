x=list(map(str,raw_input("Enter strings separate by commas:").split(',')))
y=[x[i][0] for i in range (len(x))]
print(y)
