from os import system

num1 = int(input())
num2 = int(input())
operator = input()

if operator == "+":
    _ = system('cls')
    print(num1 + num2)
elif operator == "-":
    _ = system('cls')
    print(num1 - num2)
elif operator == "/":
    _ = system('cls')
    print(num1 / num2)
elif operator == "*":
    _ = system('cls')
    print(num1 * num2)
elif operator == "//":
    _ = system('cls')
    print(num1 // num2)
elif operator == "**":
    _ = system('cls')
    print(num1 ** num2)
elif operator == "%":
    _ = system('cls')
    print(num1 % num2)

else:
    print("you are stupid")










