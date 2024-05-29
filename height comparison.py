# enter and ompare heights of John, Bob, and Alice  
height_john = float(input("Enter the height of John (in cm): "))
height_bob = float(input("Enter the height of Bob (in cm): "))
height_alice = float(input("Enter the height of Alice (in cm): "))

# Determine the tallest student
if height_john > height_bob and height_john > height_alice:
    tallest = "John"
    tallest_height = height_john
elif height_bob > height_john and height_bob > height_alice:
    tallest = "Bob"
    tallest_height = height_bob
else:
    tallest = "Alice"
    tallest_height = height_alice

# the result
print("The tallest student is {} with a height of {} cm.".format(tallest, tallest_height))
