import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define the character sets to be used in the password
    character_set = ''
    
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation
    
    if not character_set:
        raise ValueError("At least one character set must be selected")
    
    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    # Prompt the user for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("The length must be a positive integer")
            break
        except ValueError as e:
            print(e)
    
    # Ask the user for complexity options
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    # Generate and display the password
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
