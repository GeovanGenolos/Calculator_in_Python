while True:
    operator = input("Enter an operator (+ - * /): ")
    if operator == 'x': # This is to stop the program.
        break
    elif operator not in ['+', '-', '*', '/']:
        print(f"{operator} is not a valid operator")
        continue # This is to, of course, continue the program.

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print(round(result, 3))