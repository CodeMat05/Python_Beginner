
print("*******Simple Calculator*******")

operator = input("Enter an Operator (+, -, *, /): ")
num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))

if operator == "+":
    sum = num1 + num2
    print(f"The total of {num1} and {num2} is {round(sum, 2)}.")
elif operator == "-":
    difference = num1 - num2
    print(f"The difference of {num1} and {num2} is {round(difference, 2)}.")
elif operator == "*":
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {round(product, 2)}.")
elif operator == "/":
    if num2 == 0:
        print("Any number divided by zero is undefined!")
    else:
        quotient = num1 / num2
        print(f"The quotient of {num1} and {num2} is {round(quotient, 2)}")
else:
    print(f"'{operator}' is not valid operator!")
