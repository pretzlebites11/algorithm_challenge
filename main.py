import math
# This code does math and compaires numbers that the user inputs
# This code works bets with large numbers, either positive or negitive
# Prompt the user to input a number
number = float(input("Enter a number: "))

# Initialize result variable
result = 0

# Check if the number is negative, positive, or zero
if number < 0:
    print("The number is negative.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is positive.")

# Determine the range of the number
if number < -1000000:
    print("The number is less than -1000000.")
elif -1000000 <= number < -1000:
    print("The number is between -1000000 and -1000.")
elif -1000 <= number < 0:
    print("The number is between -1000 and 0.")
elif number == 0:
    print("The number is zero.")
elif 0 < number <= 1000:
    print("The number is between 0 and 1000.")
elif 1000 < number <= 1000000:
    print("The number is between 1000 and 1000000.")
else:
    print("The number is greater than 1000000.")

# Perform math operations based on the conditions
if number >= 1000000:
    # Prompt the user to input another number
    another_number = float(input("Enter another number: "))
    
    # Compare the original number with the another_number
    if number > another_number:
        print("The original number is greater than the another number.")
    elif number < another_number:
        print("The original number is less than the another number.")
    else:
        print("The original number is equal to the another number.")
        
    # Multiply the resulting number by the constant pi rounded to 5 decimal places
    result = number * round(math.pi, 5)
    
    # Prompt the user to input another number
    additional_number = float(input("Enter another number: "))
    
    # Perform operations based on the additional input
    if additional_number > 10:
        result += additional_number
    elif additional_number > 1:
        result /= additional_number
    elif additional_number <= 1:
        result -= additional_number

    print("Final result:", round(result, 5))
    
elif 1000 <= number < 1000000:
    # If the original number is between 1000 and 1000000, do some math
    result = (number / 100) * 7
    print("After dividing the number by 100 and multiplying by 7, the result is:", round(result, 5))
    
    # Multiply the resulting number by the constant pi rounded to 5 decimal places
    result *= round(math.pi, 5)
    
    # Prompt the user to input another number
    additional_number = float(input("Enter another number: "))
    
    # Perform operations based on the additional input
    if additional_number > 10:
        result += additional_number
    elif additional_number > 1:
        result /= additional_number
    elif additional_number <= 1:
        result -= additional_number

    print("Final result:", round(result, 5))
    
elif -1000000 <= number < -1000:
    # If the original number is between -1000000 and -1000, do some math
    result = (number / 200) * 7
    print("After dividing the number by 200 and multiplying by 7, the result is:", round(result, 5))
    
    # Multiply the resulting number by the constant pi rounded to 5 decimal places
    result *= round(math.pi, 5)
    
    # Prompt the user to input another number
    additional_number = float(input("Enter another number: "))
    
    # Perform operations based on the additional input
    if additional_number > 10:
        result += additional_number
    elif additional_number > 1:
        result /= additional_number
    elif additional_number <= 1:
        result -= additional_number

    print("Final result:", round(result, 5))

# Additional statements that modify the "Final result"
if result < 50:
    result += 100
    print("Final result is less than 50. Adding 100 to it:", round(result, 5))

if result > 200:
    result = math.sqrt(result)
    print("Final result is greater than 200. Taking its square root:", round(result, 5))
