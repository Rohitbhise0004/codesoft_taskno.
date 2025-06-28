contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(" Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n Contact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\n🔍 Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print(" Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if name == contact["name"].lower():
            print("Leave field blank to keep existing value.")
            new_phone = input(f"New phone ({contact['phone']}): ") or contact["phone"]
            new_email = input(f"New email ({contact['email']}): ") or contact["email"]
            new_address = input(f"New address ({contact['address']}): ") or contact["address"]
            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address
            print(" Contact updated successfully!")
            return
    print(" Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if name == contact["name"].lower():
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!")
            return
    print(" Contact not found.")

def show_menu():
    print("\n Contact Management System")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print(" Exiting Contact Manager. Goodbye!")
        break
    else:
        print(" Invalid choice. Please select between 1-6.")
