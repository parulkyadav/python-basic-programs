def fab(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(num-2):
        t=a
        a=b
        b=t+a
        print(b)

if __name__=="__main__":
    num=int(input("Enter the number of series : "))
    fab(num)
