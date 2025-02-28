# while_loop_sentinel.py

# Initialize the sum variable
total_sum = 0

# Start an infinite loop
while True:
    # Prompt the user for input
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    # Check if the sentinel value 'stop' is entered
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
    
    try:
        # Convert input to a number and add to total_sum
        number = float(user_input)
        total_sum += number
    except ValueError:
        # Handle non-numeric input
        print("Invalid input. Please enter a numeric value or 'stop'.")
        break  # Exit the loop
 
# Print the final total sum
print("The total sum is:", total_sum)
