from calcultor_logo import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print(logo)


def calculator():
    num1 = float(input('What is the first number? '))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation = input('Pick an operation: ')
        if operation not in list(operations.keys()):
            print('Invalid Symbol')
            calculator()
        num2 = float(input('What is the next number? '))
        function = operations[operation]
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        result = input(f'Do you want to continue calculating with {answer}? yes or no? ')

        if result == 'yes':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
