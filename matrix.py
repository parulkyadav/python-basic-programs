row=int(input("Enter the number of rows for matrix : "))
col=int(input("Enter the number of cols for matrix : "))
matrix = []
for i in range(row):
    column = []
    for j in range(col):
        data=int(input("Enter value for [{}][{}] : ".format(i,j)))
        column.append(data)
    print()
    matrix.append(column)

for a in matrix:
    print(*a,sep='\t',end='\n')


row1=int(input("Enter the number of rows for matrix 1 : "))
col1=int(input("Enter the number of cols for matrix 1 : "))
matrix1 = []
for i in range(row1):
    column1 = []
    for j in range(col1):
        data=int(input("Enter value for [{}][{}] : ".format(i,j)))
        column1.append(data)
    print()
    matrix1.append(column1)

for a in matrix1:
    print(*a,sep='\t',end='\n')




