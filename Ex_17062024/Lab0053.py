def say_hello_argument_default(name ="Avneet"):
    print("Hello " + name)
say_hello_argument_default("John")
say_hello_argument_default()
say_hello_argument_default(name="Jane")

def sum_of_numbers(num1, num2):
    return num1+num2

#result = sum_of_numbers(10,20)
result = sum_of_numbers(5,9)
print(result)