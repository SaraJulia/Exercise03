import arithmetic

def main():
    while True:
        input = raw_input("--> ")
        tokens = input.split()
        if tokens[0] == "q":
            quit()

        listofnums = []
        i = 1
        while i < len(tokens):
            listofnums = listofnums + [float(tokens[i])]
            i += 1

        if tokens[0] == "+":
            print arithmetic.add(listofnums)
        elif tokens[0] == "-":
            print arithmetic.subtract(listofnums)
        elif tokens[0] == "*":
            print arithmetic.multiply(listofnums)
        elif tokens[0] == "/":
            print arithmetic.divide(listofnums)
        elif tokens[0] == "square":
            if len(tokens) != 2:
                print "The square function takes only one argument." 
            else:
                print arithmetic.square(float(tokens[1]))
        elif tokens[0] == "cube":
            if len(tokens) != 2:
                print "The cube function requires two arguments."
            else:
                print arithmetic.cube(float(tokens[1]))
        elif tokens[0] == "pow":
            if len(tokens) != 3:
                print "The power function requires two arguments."
            else:
                print arithmetic.power(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "mod":
            if len(tokens) != 3:
                print "The mod function requires two arguments."
            else:
                print arithmetic.mod(float(tokens[1]), float(tokens[2]))
        else:
            print "Enter a valid expression."

if __name__ == "__main__":
    main()