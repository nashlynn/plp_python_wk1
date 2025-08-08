number1 = float(input("please enter first number: "))
number2 = float(input("please enter second number: "))
operation = input("please enter operation on numbers (+,-,*, or / ): ")

if operation == "+":
    answer = number1 + number2
    print(f"{number1} + {number2} = {answer}")

if operation == "-":
    answer = number1 - number2
    print(f"{number1} - {number2} = {answer}")

if operation == "*":
    answer = number1 * number2
    print(f"{number1} * {number2} = {answer}")

if operation == "/":
    answer = number1 / number2
    print(f"{number1} / {number2} = {answer}")

