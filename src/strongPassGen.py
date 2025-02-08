import random

print('            Welcome to the strong password generator!')
print('--This program will generate a reliable strong password for your use--')

def generate_password():
    # Define the characters to be used in the password
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234567890"
    special = "!@#$%^&*()_+"
    all_characters = lower + upper + digits + special
    
    # Ensure the password has at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random characters from all categories
    for i in range(12):
        password.append(random.choice(all_characters))
    
    # Shuffle the list to ensure randomness and convert to a string
    random.shuffle(password)
    return ''.join(password)

input('Press Enter to generate a strong password: ')
print('Generated password:', generate_password())

