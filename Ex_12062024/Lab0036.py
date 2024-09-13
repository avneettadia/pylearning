#Problem to find the max number between two numbers

a=int(input("Enter First Number\n"))
b=int(input("Enter Second Number\n"))
result=max(a,b)
print("The maximum number is: ", result)
if (a>b):
    print("The maximum number is: ", a)
else:
    print("The maximum number is: ", b)
