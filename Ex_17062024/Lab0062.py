n = int(input("Enter the Fabonacci Series Number\n"))
a=0
b=1
for i in range(0, n + 1):
    c = a+b
    a=b
    b=c
    print(c)
