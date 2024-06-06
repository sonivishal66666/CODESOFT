def main():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print("Press 'a' for addition")
    print("Press 'b' for subtraction")
    print("Press 'c' for multiplication")
    print("Press 'd' for division")
    print("Press 'e' for remainder")
    
    x = input("Enter your choice: ")

    if x == 'a':
        print("The addition =", num1 + num2)
    elif x == 'b':
        print("The subtraction =", num1 - num2)
    elif x == 'c':
        print("The multiplication =", num1 * num2)
    elif x == 'd':
        if num2 != 0:
            print("The division =", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    elif x == 'e':
        if num2 != 0:
            print("The remainder =", num1 % num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
