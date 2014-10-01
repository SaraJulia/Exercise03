import arithmetic.py

while True:
    input = raw_input("--> ")
    tokens = input.split(" ")
    if tokens[0] == "q":
        quit()
    elif tokens[0] == "+":
        print add(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == "-":
        print subtract(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == "*":
        print multiply(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == "/":
        print divide(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == "square":
        print square(float(tokens[1]))
    elif tokens[0] == "cube":
        print cube(float(tokens[1]))
    elif tokens[0] == "pow":
        print power(float(tokens[1]),float(tokens[2]))
    elif tokens[0] == "mod":
        print mod(float(tokens[1]),float(tokens[2]))
    else:
        print "enter a valid expression"