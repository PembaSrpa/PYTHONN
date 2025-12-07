# Web scraping + Database + Fie OPerations: Scrape data, store it in SQL & export to CSV/JSON
from scraper import scrape_books
from database import init_db
from exporter import export_csv, export_json

def menu():
    print("\n--- Web Scraper + Database + Exporter ---")
    print("1. Initialize Database")
    print("2. Scrape & Save Data")
    print("3. Export to CSV")
    print("4. Export to JSON")
    print("5. Exit")


def main():
    while True:
        menu()
        c = input("Enter choice: ")

        if c == "1":
            init_db()
            print("Database initialized.")
        elif c == "2":
            scrape_books()
        elif c == "3":
            export_csv()
        elif c == "4":
            export_json()
        elif c == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
