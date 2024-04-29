# File for Adding the features
def addition(number1, number2):
    inputInfo=f"{getPositiveorNegativeStatus(number1)}; + {getPositiveorNegativeStatus(number2)};"
    equation =f"{number1} + {number2}"
    result = number1 + number2
    outputInfo = f"{getPositiveorNegativeStatus(result)}"
    return f"{equation} = {result}\n{inputInfo} = {outputInfo};"

def subtraction(number1, number2):
    inputInfo=f"{getPositiveorNegativeStatus(number1)}; + {getPositiveorNegativeStatus(number2)};"
    equation =f"{number1} + {number2}"
    result = number1 - number2
    outputInfo = f"{getPositiveorNegativeStatus(result)}"
    return f"{equation}  = {result}\n{inputInfo} = {outputInfo}" 

def multiplication(number1, number2):
    inputInfo=f"{getPositiveorNegativeStatus(number1)}; + {getPositiveorNegativeStatus(number2)};"
    equation =f"{number1} + {number2}"
    result = number1 * number2
    outputInfo = f"{getPositiveorNegativeStatus(result)}"
    return f"{equation}  = {result}\n{inputInfo} = {outputInfo}" 

def division(number1, number2):
    inputInfo=f"{getPositiveorNegativeStatus(number1)}; + {getPositiveorNegativeStatus(number2)};"
    equation =f"{number1} + {number2}"
    result = number1 // number2
    outputInfo = f"{getPositiveorNegativeStatus(result)}"
    return f"{equation}  = {result}\n{inputInfo} = {outputInfo}" 

def getPositiveorNegativeStatus(number):
    if number<0:
        positive_negative = "Negative"
    else:
        positive_negative ="Positve"

        return f"{positive_negative}" 

def getEvenOrOddStatus(number):
    if number % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"
    return f"{even_odd}"


def formattedOutput(number1, number2, operation):
    result = getResult(number1, number2, operation)
    line1 = f"{number1} {operation} {number2} = {result}"
    line1 += f"{getPositiveorNegativeStatus(number1) | getEvenOrOddStatus(number1)} {operation} {getPositiveorNegativeStatus(number2) | getEvenOrOddStatus(number2)} = {getPositiveorNegativeStatus(result) | getEvenOrOddStatus(result)}"
    return line1



def getResult(number1, number2, operation):
    if operation == "+":
        return addition(number1, number2)
    elif operation == "-":
        return subtraction(number1, number2)
    elif operation == "/":
        return division(number1, number2)
    elif operation == "*":
        return multiplication(number1, number2)
    
    return "No valid operation found for the given input"
    
        

    
print(addition(40,60))
print(addition(41,60))
print(addition(41,61))
print(addition(40,67))
