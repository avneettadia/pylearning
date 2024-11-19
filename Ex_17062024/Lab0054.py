def say_hello_arg_default(name="Avneet"):
    print("hello", name)

say_hello_arg_default()
say_hello_arg_default(name="Loveleen")
say_hello_arg_default("Drivu")

def sum_number_argument_ret(a,b):
    return a+b
#result = sum_number_argument_ret(3,4)
result = sum_number_argument_ret(a=3,b=5)
print(result)
