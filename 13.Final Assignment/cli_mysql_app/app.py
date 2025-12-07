# design a CLI app with basic CRUD opertaions and database integration

from db import create_user, get_users, get_user, update_user, delete_user


def menu():
    print("\n--- USER MANAGEMENT CLI (MySQL) ---")
    print("1. Create User")
    print("2. List Users")
    print("3. Get User by ID")
    print("4. Update User")
    print("5. Delete User")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = input("Choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            create_user(name, email)
            print("User created.")

        elif choice == "2":
            for u in get_users():
                print(u)
            input("Press Enter to continue...")

        elif choice == "3":
            uid = int(input("User ID: "))
            print(get_user(uid))
            input("Press Enter to continue...")

        elif choice == "4":
            uid = int(input("User ID: "))
            name = input("New Name: ")
            email = input("New Email: ")
            update_user(uid, name, email)
            print("User updated.")

        elif choice == "5":
            uid = int(input("User ID: "))
            delete_user(uid)
            print("User deleted.")

        elif choice == "6":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
