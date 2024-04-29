from calc import formattedOutput, parseOperator

number1 = int(input("Enter your number"))
number2 = int(input("Enter your number"))

operation = parseOperator(input("""Enter a symbol:
a for +
s for -
m for X
d for %
"""))

if __name__ == "__main__":
    print(formattedOutput(number1, number2, operation))