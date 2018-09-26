row1 = int(input("Enter the number of rows for matrix1 : "))
col1 = int(input("Enter the number of columns for matrix1 : "))

matrix1=[]
for i in range(row1):
    column1=[]
    for j in range(col1):
        data=int(input("Enter value for [{}][{}]".format(i,j)))
        column1.append(data)
    matrix1.append(column1)
    print()


print("----------------------------------------------------")
row2=int(input("Enter the number of rows for matrix2 : "))
col2=int(input("Enter the number of columns for matrix2 : "))

matrix2=[]
for i in range(row2):
    column2=[]
    for j in range(col2):
        data=int(input("Enter the value of [{}][{}] : ".format(i,j)))
        column2.append(data)
    matrix2.append(column2)
    print()

print("Matrix 1 : ")
for a in matrix1:
    print(*a, sep="\t", end="\n")

print("Matrix 2 : ")
for data in matrix2:
    print(*data,sep='\t',end='\n')


if row1==row2 and col1==col2 :
    matrixadd=[]
    for i in range(row1):
        columnadd=[]
        for j in range(col1):
            dataadd=matrix1[i][j]+matrix2[i][j]
            columnadd.append(dataadd)
        matrixadd.append(columnadd)
        print()

    print("Addition of matrix1 and matrix2 : ")
    for p in matrixadd:
        print(*p,sep='\t',end='\n')


    matrixmul=[]

    
    

else :
    print("galat h")






















