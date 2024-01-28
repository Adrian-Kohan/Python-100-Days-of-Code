from art import logo

from replit import clear
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

operations = {
    "*" : multiply,
    "+" : add,
    "-" : subtract,
    "/" : divide
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)


    continue_calculating = True

    while continue_calculating:
        operation_symbol =input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        for operator in operations:
            function = operations[operation_symbol]
            answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        answer2 = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if answer2 == "y":
            num1 = answer
        else:
            continue_calculating = False
            clear()
            calculator()
calculator()
