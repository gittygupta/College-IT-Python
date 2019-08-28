m,n=list(map(int,raw_input("Enter dimensions of mat separate by comma:").split(",")))
print("enter elements of mat1")
mat1=[[int(input()) for i in range(n)] for i in range (m)]

print("enter elements of mat2")
mat2=[[int(input()) for i in range(n)] for i in range(m)]
mat3=[[0 for x in range(n)]for i in range(m)]
for i in range (m):
    for j in range (n):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
for i in mat3:
   print(i)
   print('\n')
