# Coding Task:
# contacts = {}
# def add_contact():
#     name = input("Enter name: ")
#     phno = int(input("Enter Phno: "))
#     contacts[name] = phno
#     print("Contact added successfully")
# def view_contact():
#     if not contacts:
#         print("Contact not found")
#     else:
#         for name, phno in contacts.items():
#             print("Name:",name, "| Phone:",phno)
# def update_contact():
#     name = input("Enter new name: ")
#     if name in contacts:
#         new_phno = input("Enter New Phno: ")
#         contacts[name] = new_phno
#         print("Contact Updated")
#     else:
#         print("contact not found")
# def delete_contact():
#     name = input("Enter name to delete: ")
#     if name in contacts:
#         del contacts[name]
#         print("Contact deleted successfully")
#     else:
#         print("Contact not found")
#
# while True:
#     print("\n--- Contact Book ---")
#     print("1. Add Contact")
#     print("2. View Contacts")
#     print("3. Update Contact")
#     print("4. Delete Contact")
#     print("5. Exit")
#
#     choice = input("enter ur choice: ")
#
#     if choice == "1":
#         add_contact()
#     elif choice == "2":
#         view_contact()
#     elif choice == "3":
#         update_contact()
#     elif choice == "4":
#         delete_contact()
#     elif choice == "5":
#         print("Exiting from contact book")
#         break
#     else:
#         print("Invalid choice. Try Again")





# Assignment:
import json
contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully.")
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contacts ---")
        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)
def search_contact():
    name = input("Enter name to search: ")
    phone = contacts.get(name)
    if phone:
        print("Name:", name)
        print("Phone:", phone)
    else:
        print("Contact not found.")
def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        print("Contact updated successfully.")
    else:
        print("Contact not found.")
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
    print("Contacts saved successfully.")
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
load_contacts()

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        save_contacts()
    elif choice == "7":
        save_contacts()
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")