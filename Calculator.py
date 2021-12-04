from art import logo

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        answer_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if answer_continue == "n":
            calculator()
            

calculator()
