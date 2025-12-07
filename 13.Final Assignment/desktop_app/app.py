# Data entry application
# Develop an application to manage data in JSON/CSV format

from storage import load_json, save_json, export_csv, import_csv

def menu():
    print("\n--- DATA ENTRY APPLICATION ---")
    print("1. Add Record")
    print("2. List Records")
    print("3. Search Record by ID")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Export to CSV")
    print("7. Import from CSV")
    print("8. Exit")


def add_record():
    data = load_json()
    record = {}
    record["id"] = input("Enter ID: ")
    record["name"] = input("Enter Name: ")
    record["age"] = input("Enter Age: ")
    data.append(record)
    save_json(data)
    print("Record added!")


def list_records():
    data = load_json()
    for item in data:
        print(item)
    input("Press Enter to continue...")


def search_record():
    rid = input("Enter ID: ")
    data = load_json()
    for rec in data:
        if rec["id"] == rid:
            print(rec)
            return
        input("Press Enter to continue...")
    print("Record not found.")


def update_record():
    rid = input("Enter ID: ")
    data = load_json()

    for rec in data:
        if rec["id"] == rid:
            rec["name"] = input("New Name: ")
            rec["age"] = input("New Age: ")
            save_json(data)
            print("Record updated.")
            return

    print("Record not found.")


def delete_record():
    rid = input("Enter ID: ")
    data = load_json()
    new_data = [rec for rec in data if rec["id"] != rid]

    if len(new_data) == len(data):
        print("Record not found.")
    else:
        save_json(new_data)
        print("Record deleted.")


def main():
    while True:
        menu()
        choice = input("Choice: ")

        if choice == "1": add_record()
        elif choice == "2": list_records()
        elif choice == "3": search_record()
        elif choice == "4": update_record()
        elif choice == "5": delete_record()
        elif choice == "6": export_csv()
        elif choice == "7": 
            fname = input("CSV filename: ")
            import_csv(fname)
        elif choice == "8": 
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()