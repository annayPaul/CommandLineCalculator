# File for Adding the features
def addition(number1, number2):
    inputInfo = f"{getEvenOrOddStatus(number1)}; + {getEvenOrOddStatus(number2)};"
    equation = f"{number1} + {number2}"
    result = number1 + number2
    outputInfo = f"{getEvenOrOddStatus(result)}"
    return f"{equation} = {result}\n{inputInfo} = {outputInfo}"

def subtraction(number1, number2):
    inputInfo = f"{getEvenOrOddStatus(number1)}; - {getEvenOrOddStatus(number2)};"
    equation = f"{number1} - {number2}"
    result = number1 + number2
    outputInfo = f"{getEvenOrOddStatus(result)}"
    return f"{equation} = {result}\n{inputInfo} = {outputInfo}"

def multiplication(number1, number2):
    inputInfo = f"{getEvenOrOddStatus(number1)}; * {getEvenOrOddStatus(number2)};"
    equation = f"{number1} * {number2}"
    result = number1 * number2
    outputInfo = f"{getEvenOrOddStatus(result)}"
    return f"{equation} = {result}\n{inputInfo} = {outputInfo}"

def division(number1, number2):
    inputInfo = f"{getEvenOrOddStatus(number1)}; / {getEvenOrOddStatus(number2)};"
    equation = f"{number1} / {number2}"
    result = number1 // number2
    outputInfo = f"{getEvenOrOddStatus(result)}"
    return f"{equation} = {result}\n{inputInfo} = {outputInfo}"

def getEvenOrOddStatus(number):
    if number % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"
    return f"{even_odd}"