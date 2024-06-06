import os

def banner():
    print("     CONTACT INFORMATION MANAGER    ")

def add_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    save = input("Save? (y/n): ")
    if save.lower() == 'y':
        with open("contacts.txt", "a") as fout:
            fout.write(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}\n")
        more = input("Do you want to add more contacts? (y/n): ")
        if more.lower() == 'y':
            add_contact()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Contacts added successfully.")

def show_contacts():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    print("Contacts:")
    with open("contacts.txt", "r") as fin:
        for line in fin:
            print(line.strip())

def search_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    search_term = input("Enter name or phone number to search: ")
    found = False
    with open("contacts.txt", "r") as fin:
        for line in fin:
            if search_term in line:
                print(f"Contact found: {line.strip()}")
                found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    search_term = input("Enter name or phone number of the contact to delete: ")
    found = False
    with open("contacts.txt", "r") as fin, open("temp.txt", "w") as temp:
        for line in fin:
            if search_term in line:
                print(f"Contact deleted: {line.strip()}")
                found = True
            else:
                temp.write(line)
    if not found:
        print("Contact not found.")
    os.remove("contacts.txt")
    os.rename("temp.txt", "contacts.txt")

def update_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    search_term = input("Enter name or phone number of the contact to update: ")
    found = False
    with open("contacts.txt", "r") as fin, open("temp.txt", "w") as temp:
        for line in fin:
            if search_term in line:
                print(f"Current contact: {line.strip()}")
                name = input("Enter new Name: ")
                phone = input("Enter new Phone Number: ")
                email = input("Enter new Email: ")
                address = input("Enter new Address: ")
                temp.write(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}\n")
                print("Contact updated successfully.")
                found = True
            else:
                temp.write(line)
    if not found:
        print("Contact not found.")
    os.remove("contacts.txt")
    os.rename("temp.txt", "contacts.txt")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        banner()
        print("\t1. Add contact")
        print("\t2. Show contacts")
        print("\t3. Search contact")
        print("\t4. Delete contact")
        print("\t5. Update contact")
        choice = input("Enter choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
