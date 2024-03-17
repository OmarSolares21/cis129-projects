# Initialize loop control variable with an explicit initial value
number = 0  # Setting the initial value

# Loop starts here
while True:
    # Asking for user input
    number = int(input("Please enter a number (negative to stop): "))
    
    # Printing the entered number
    print(f"You entered: {number}")
    
    # Checking if the entered number is negative to break the loop
    if number < 0:
        break  # Exiting the loop

# This line runs after the loop ends
print("You've entered a negative number. Exiting the loop.")