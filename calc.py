# File for Adding the features
def addition(number1, number2):
    inputInfo=f"{getPositiveorNegativeStatus(number1)}; + {getPositiveorNegativeStatus(number2)};"
    equation =f"{number1} + {number2}"
    result = number1 + number2
    outputInfo = f"{getPositiveorNegativeStatus(result)}"
    return f"{equation}  = {result}\n{inputInfo} = {outputInfo}" 

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