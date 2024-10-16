def allowed_to_enter_class(name):
    match name:
        case "John":
            print("John is allowed to enter the class")
        case "Jane":
            print("Jane is allowed to enter the class")
        case "Bob":
            print("Bob is not allowed to enter the class")
        case _:
            print("You are not allowed to enter the class")

allowed_to_enter_class("John")