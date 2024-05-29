#divisibility test by 7 and 11
number = int(input("Enter a number: "))

# Check divisibility
if number % 7 == 0 and number % 11 == 0:
    result = "The number {} is divisible by both 7 and 11.".format(number)
else:
    result = "The number {} is not divisible by both 7 and 11.".format(number)

# Output the result
print(result)