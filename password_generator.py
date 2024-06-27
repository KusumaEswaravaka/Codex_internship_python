import random
import string

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Get the desired password length from the user
try:
    password_length = int(input("Enter the desired length for your password: "))
    
    if password_length <= 0:
        print("Please enter a positive number for the password length.")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated Password: {generated_password}")

except ValueError:
    print("Invalid input. Please enter a numeric value for the password length.")
