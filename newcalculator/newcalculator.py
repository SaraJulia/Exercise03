import newarithmetic

def function_call(command, args):
    dispatch = { 
        '+': newarithmetic.add,
        '-': newarithmetic.subtract,
        '*': newarithmetic.multiply,
        '/': newarithmetic.divide,
        'square': newarithmetic.square,
        'cube': newarithmetic.cube,
        'pow': newarithmetic.power,
        'mod': newarithmetic.mod
    }
    if command not in dispatch:
        print "Please enter a valid expression." # add guide
    else:   
        return dispatch[command](args)


def main():
    while True:
        input = raw_input("--> ")
        tokens = input.split()


        if tokens[0] == "q":
            quit()
        else:
            operator = tokens[0]

        listofnums = []
        i = 1
        while i < len(tokens):
            listofnums = listofnums + [float(tokens[i])]
            i += 1

        print function_call(operator,listofnums)
            

if __name__ == "__main__":
    main()