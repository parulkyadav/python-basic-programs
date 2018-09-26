n=int(input("Enter the number of series : "))
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()

print("--------------------------------------------\n")


i=1
while i <= n :
    
    k=n-1
    while k >= i :
        print(" ",end=" ")
        k-=1
    j=1
    while j <= i:
       
        print("*",end=" ")
        j+=1
    print()
    i+=1


print("-------------------------------------------\n")


for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()

print("-------------------------------------------\n")


i=1
p=n
while i <= n:
    k=2
    while k <= i :
        print(" ",end=" ")
        k+=1
    j=p
    while j >= 1 :
        print("*",end=" ")
        j-=1
    print()
    p-=1
    i+=1

print("-------------------------------------------\n")


i=1
p=n
while i <= n :
    k=p
    while k > 1 :
        print(" ",end=" ")
        k-=1
    j=1
    while j <= i :
        print("*",end=" ")
        j+=1
    m=2
    while m <= i :
        print("*",end=" ")
        m+=1
    print()
    p-=1
    i+=1

print("---------------------------------------------\n")

i=1
x=n
while i <= n :
    k=1
    while k < i :
        print(" ",end=" ")
        k+=1
    j=x
    while j >= 1 :
        print("*",end=" ")
        j -=1
    p=x
    while p > 1 :
        print("*",end=" ")
        p-=1
    print()
    x -= 1
    i += 1

print("-----------------------------------------------\n")

for i in range(n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()


print("-----------------------------------------------\n")

for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()

print("-----------------------------------------------\n")
k=1
for i in range(n+1):
    for j in range(i):
        print(k,end=" ")
        k += 1
    print()

print("-----------------------------------------------\n")


i=1
p=n
while i <= n :
    k=p
    while  k > 1 :
        print(" ",end="")
        k -= 1
    j=1
    while j <= i :
        print(j,end=" ")
        j +=1
    k +=1
    p -=1
    i += 1
    print()
