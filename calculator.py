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
            print arithmetic.square(tokens[1])
        elif tokens[0] == "cube":
            print arithmetic.cube(tokens[1])
        elif tokens[0] == "pow":
            print arithmetic.power(listofnums)
        elif tokens[0] == "mod":
            print artnthmetic.mod(listofnums)
        else:
            print "enter a valid expression"

if __name__ == "__main__":
    main()