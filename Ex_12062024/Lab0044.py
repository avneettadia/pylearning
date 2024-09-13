a=int(input("enter the first side of triangle:\n"))
b=int(input("enter the second side of triangle:\n"))
c=int(input("enter the third side of triangle"))
if a==b==c:
    print("Its an equilateral triangle")
elif a==b or b==c or a==c:
    print("Its an isosceles triangle")
else:
    print("Its a scalene triangle")