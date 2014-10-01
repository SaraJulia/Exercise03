import arithmetic

def main():
    while True:
        input = raw_input("--> ")
        tokens = input.split()
        if tokens[0] == "q":
            quit()
        first = float(tokens[1])
        second = float(tokens[2])
        if tokens[0] == "+":
            print arithmetic.add(first,second)
        elif tokens[0] == "-":
            print arithmetic.subtract(first,second)
        elif tokens[0] == "*":
            print arithmetic.multiply(first,second)
        elif tokens[0] == "/":
            print arithmetic.divide(first,second)
        elif tokens[0] == "square":
            print arithmetic.square(first)
        elif tokens[0] == "cube":
            print arithmetic.cube(first)
        elif tokens[0] == "pow":
            print arithmetic.power(first,second)
        elif tokens[0] == "mod":
            print arithmetic.mod(first,second)
        else:
            print "enter a valid expression"

if __name__ == "__main__":
    main()