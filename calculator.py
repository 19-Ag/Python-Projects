def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero!")
    return n1 / n2

calculator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation(n1, n2, symbol):
    return calculator_dict[symbol](n1, n2)

result = None

while True:
    if result is None:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
    else:
        n1 = result
        use_previous_result = input("Do you want to use the previous result? (yes/no): ").lower()
        if use_previous_result == "yes":
            n2 = int(input("Enter second number: "))
        else:
            n1 = int(input("Enter first number: "))
            n2 = int(input("Enter second number: "))

    print("This is the list of available operations:")
    for symbol in calculator_dict:
        print(symbol)
    symbol = input("Enter the operation you want to perform: ")
    result = calculation(n1, n2, symbol)
    print("Result:", result)

    continue_calc = input("Do you want to continue? ").lower() == "yes"
    if not continue_calc:
        print("Thank you for using the calculator!")
        break
