def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 ** 2

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

while True:
    input = raw_input("--> ")
    tokens = input.split(" ")
    if tokens[0] == "q":
        quit()
    elif tokens[0] == "+":
        print add(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "-":
        print subtract(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "*":
        print multiply(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "/":
        print divide(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "square":
        print square(int(tokens[1]))
    elif tokens[0] == "cube":
        print cube(int(tokens[1]))
    elif tokens[0] == "pow":
        print power(int(tokens[1]),int(tokens[2]))
    elif tokens[0] == "mod":
        print mod(int(tokens[1]),int(tokens[2]))
    else:
        print "enter a valid function"