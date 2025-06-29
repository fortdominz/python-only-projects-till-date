import calculator_art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# we do not want the parenthesis of the functions, so we do not trigger the functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(calculator_art.logo)
    continue_calculating = True
    n1 = float(input("what is the first number? "))

    while continue_calculating:

        for symbol in operations:
            print(symbol)
        operation_type = input("select: ")
        n2 = float(input("what is the second number? "))

        # addition = operations["+"](n1, n2)
        # subtraction = operations["-"](n1, n2)
        # multiplication = operations["*"](n1, n2)
        # division = operations["/"](n1, n2)     # shorter way of writing all these into one is... answer = operations[operation_type](n1, n2)

        answer = operations[operation_type](n1, n2)
        print(f"{n1} {operation_type} {n2} = {answer}")
        # print(f"Invalid input! {operation_type} does not yet on this calculator. Await later updates.")

        # if operation_type == "+":
        #     print(f"{n1} {operation_type} {n2} = {answer}")
        # elif operation_type == "-":
        #     print(f"{n1} {operation_type} {n2} = {answer}")
        # elif operation_type == "*":
        #     print(f"{n1} {operation_type} {n2} = {answer}")
        # elif operation_type == "/":
        #     print(f"{n1} {operation_type} {n2} = {answer}")
        # else:
        #     print(f"Invalid input! {operation_type} does not yet on this calculator. Await later updates.")

        print("Do you still want to coninue calculating or restart with new calculations? ")
        calculation_status = input("Type 'y' to continue or 'n' to restart: \n")
        if calculation_status == 'y':
            n1 = answer
        elif calculation_status == 'n':
            continue_calculating = False
            print("\n " * 200)
            calculator()
        else:
            print("Invalid input! Session Terminated. Next time, type 'y' to continue ")
            calculator()

calculator()