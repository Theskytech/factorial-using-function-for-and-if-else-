# Python Program to Find Factorial of a Number using For loop 
# Where
# x - To store the input number
# f - To store the factorial value

print ("Enter an integer number to find the factorial-\n")

x, i, f = int(input()), 1, 1 

if x > 0:
    for i in range(1, x+1):
        f *= i
    print ("Factorial of ", x, " = ", f, "\n")
else:
    print ("Sorry, The input number should be a positive number !\n")