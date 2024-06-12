import os

# Function to display the banner
def display_banner():
    print("     CONTACT INFORMATION MANAGER    ")

# Function to add a new contact
def add_new_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    save = input("Save this contact? (y/n): ").strip().lower()
    if save == 'y':
        with open("contacts.txt", "a") as file_out:
            file_out.write(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}\n")
        add_more = input("Do you want to add more contacts? (y/n): ").strip().lower()
        if add_more == 'y':
            add_new_contact()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Contacts added successfully.")

# Function to display all contacts
def display_contacts():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    print("Contacts:")
    with open("contacts.txt", "r") as file_in:
        for line in file_in:
            print(line.strip())

# Function to search for a specific contact
def search_for_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    search_term = input("Enter name or phone number to search: ")
    found = False
    with open("contacts.txt", "r") as file_in:
        for line in file_in:
            if search_term in line:
                print(f"Contact found: {line.strip()}")
                found = True
    if not found:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    search_term = input("Enter name or phone number of the contact to delete: ")
    found = False
    with open("contacts.txt", "r") as file_in, open("temp.txt", "w") as temp_file:
        for line in file_in:
            if search_term in line:
                print(f"Contact deleted: {line.strip()}")
                found = True
            else:
                temp_file.write(line)
    if found:
        os.remove("contacts.txt")
        os.rename("temp.txt", "contacts.txt")
    else:
        print("Contact not found.")

# Function to update an existing contact
def update_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_banner()
    search_term = input("Enter name or phone number of the contact to update: ")
    found = False
    with open("contacts.txt", "r") as file_in, open("temp.txt", "w") as temp_file:
        for line in file_in:
            if search_term in line:
                print(f"Current contact: {line.strip()}")
                name = input("Enter new Name: ")
                phone = input("Enter new Phone Number: ")
                email = input("Enter new Email: ")
                address = input("Enter new Address: ")
                temp_file.write(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}\n")
                print("Contact updated successfully.")
                found = True
            else:
                temp_file.write(line)
    if found:
        os.remove("contacts.txt")
        os.rename("temp.txt", "contacts.txt")
    else:
        print("Contact not found.")

# Main function to display the menu and handle user input
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        display_banner()
        print("\t1. Add contact")
        print("\t2. Show contacts")
        print("\t3. Search contact")
        print("\t4. Delete contact")
        print("\t5. Update contact")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_new_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            search_for_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
