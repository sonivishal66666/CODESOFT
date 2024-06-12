import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
    # Initialize the character pool
    characters = ''
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    # Ensure at least one character set is selected
    if not characters:
        raise ValueError("At least one type of characters must be selected")
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt user for the length of the password
    while True:
        try:
            pwd_length = int(input("Enter the desired length of the password: "))
            if pwd_length <= 0:
                raise ValueError("Password length must be a positive integer")
            break
        except ValueError as err:
            print(err)
    
    # Ask user about character inclusion
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    # Generate and display the password
    try:
        password = generate_password(pwd_length, include_uppercase, include_lowercase, include_digits, include_special_chars)
        print("Generated Password:", password)
    except ValueError as err:
        print(err)

if __name__ == "__main__":
    main()
