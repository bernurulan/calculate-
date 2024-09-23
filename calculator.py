num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operator = input("Enter operator:")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "//":
    print(num1 // num2)
elif operator == "**":
    print(num1 ** num2)
elif operator == "%":
    print(num1 % num2)

else:
    print("you are stupid")


def calculate(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)


calculate(3, 4, "+")


