import json
from json_csv_functions import (
    get_extension,
    init_db,
    add_record,
    view_records,
    search_record,
    delete_record,
)


def main():
    print("--- JSON/CSV Database Manager ---")
    filename = input("Enter filename: ").strip()

    while True:
        print(f"\nCurrently managing: {filename}")
        print("1. Initialize DB (New/Overwrite)")
        print("2. Add Record")
        print("3. View All Records")
        print("4. Search Record")
        print("5. Delete Record")
        print("6. Change File")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            h = input("Enter headers separated by commas: ").split(",")
            headers = [item.strip() for item in h]
            init_db(filename, headers)

        elif choice == "2":
            headers = []
            ext = get_extension(filename)

            if ext == ".json":
                with open(filename, "r", encoding="utf-8") as f:
                    headers = json.load(f).get("schema", [])
            elif ext == ".csv":
                with open(filename, "r", encoding="utf-8") as f:
                    headers = f.readline().strip().split(",")

            record = {}
            print(f"Adding record to {filename}:")
            for column in headers:
                val = input(f"Enter value for '{column}': ")
                record[column] = val

            add_record(filename, record)
            print("Record added successfully.")

        elif choice == "3":
            view_records(filename)

        elif choice == "4":
            f = input("Field to search: ")
            v = input("Value to find: ")
            search_record(filename, f, v)

        elif choice == "5":
            f = input("Field to target: ")
            v = input("Value to delete: ")
            delete_record(filename, f, v)

        elif choice == "6":
            filename = input("Enter new filename: ").strip()

        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid selection.")


main()
