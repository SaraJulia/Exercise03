def add(nums):
    thesum = 0
    i = 0
    while i < len(nums):
        thesum = thesum + nums[i]
        i += 1
    return thesum

def subtract(nums):
    thediff = nums[0] - nums[1]
    i = 2
    while i < len(nums):
        thediff = thediff - nums[i]
        i += 1
    return thediff

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
