#a wscube@gmail.com
#0-9
#._ time1
#.2,3

#to verify email
import re

def is_valid_email(email):
    # Define the pattern to match a valid email address
    email_pattern = re.compile(r'^\w+@[a-z]+\.[a-z]{2,3}$')
    
    # Check if the email address matches the pattern
    if email_pattern.match(email):
        return True
    else:
        return False

# Get the email address from the user
email = input("Enter your email address: ")

# Validate the email address
if is_valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is not valid.")

#to generate random email 
import re
import random

def generate_email(name, surname, count=0):
    # Define the pattern to match a valid email address
    email_pattern = re.compile(r'^\w+@[a-z]+\.[a-z]{2,3}$')

    # Generate a random number between 0 and 100 to add to the email address
    random_number = str(random.randint(0, 100))

    # Create the email address by combining the name, surname, and random number
    email = name.lower() +  surname.lower() + random_number + '@gmail.com'

    # Check if the email address matches the pattern, if not, call the function again
    if not email_pattern.match(email) and count < 100:
        return generate_email(name, surname, count+1)
    
    return email

# Get the name and surname from the user
name = input("Enter your name: ")
surname = input("Enter your surname: ")

# Generate the email address
email = generate_email(name, surname)

# Print the email address
print("Your email address is: " + email)

