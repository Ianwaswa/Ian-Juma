#Prompt users to enter numbers and the operators they want to use
#Operators are +, -, *, /, %, ** and //
num1, num2 = input("Enter Two Numbers: ").split()
#Convert all string input to integers
num1 = int(num1)
num2 = int(num2)
#Operations to be performed
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
exponant = num1 ** num2

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
print("{} ** {} = {}".format(num1, num2, exponant))

#If operator is -, subtract the two numbers and print the result based on difference
#Print the result of the operation