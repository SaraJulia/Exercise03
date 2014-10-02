def add(nums):
    thesum = 0
    i = 0
    while i < len(nums):
        thesum = thesum + nums[i]
        i += 1
    return thesum

def subtract(nums):
    if len(nums) < 2:
        return nums[0]
    else:
        thediff = nums[0] - nums[1]
        i = 2
        while i < len(nums):
            thediff = thediff - nums[i]
            i += 1
        return thediff

def multiply(nums):
    product = 1
    i = 0
    while i < len(nums):
        product = product * nums[i]
        i += 1
    return product

def divide(nums):
    if len(nums) < 2:
        return nums[0]
    else:
        dividend = nums[0] / nums[1]
        i = 2
        while i < len(nums):
            dividend = dividend / nums[i]
            i += 1
        return dividend

def square(num1):
    if len(num1) != 1:
        return "Square requires one argument."
    else:
        return num1 ** 2

def cube(num1):
    if len(num1) != 1:
        return "Cube requires one argument."
    else:
        return num1 ** 3

def power(num):
    if len(num) != 2:
        return "Power requires two arguments."
    else:
        return num[0] ** num[1]

def mod(num):
    if len(num) != 2:
        return "Modulo requires two arguments."
    else:
        return num[0] % num[1]
