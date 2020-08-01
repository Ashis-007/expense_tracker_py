from datetime import date
from sys import exit
from database import Database
from spreadsheet import Spreadsheet

def input_expense():
    amount = int(input("Enter amount: "))
    note = input("Enter note/desciption: ")
    curr_date = date.today().strftime("%d/%m/%y")
    return (curr_date, amount, note)


def show_data(data):
    print("\tDATE\t\tAMOUNT\tNOTE")
    for expense in data:
        date, amount, note  = expense
        print(f"\t{date}\tRs {amount}\t{note}")

            
def export_to_spreadsheet(data):
    spreadsheet = Spreadsheet()
    spreadsheet.insert_data(data)
    spreadsheet.save_workbook()


def show_menu():
    print("""
    == MENU ==
    press 1 to add a new expense
    press 2 to see all expenses
    press 3 to see all expenses by given date
    press 4 to export your expenses into an excel file
    press 5 to exit
    press 0 to delete all data
    """)


if __name__ == "__main__":
    db = Database() # instance of class Database

    print("=== Welcome to your own personalised Expense_Tracker! ===")
    choice = 0
    while choice != 5:
        show_menu()
        choice = int(input("Choose your option: "))

        if choice == 5:
            continue

        elif choice == 1:
            data = input_expense()
            db.insert_data(data)

        elif choice == 2:
            data = db.fetch_all_data()
            if not data:
                print("No expense saved. Save some and try again.")
            else:
                show_data(data)

        elif choice == 3:
            pass

        elif choice == 4:
            data = db.fetch_all_data()
            export_to_spreadsheet(data)

        elif choice == 0:
            if input("Are you sure?(yes/no): ") == "yes":
                if db.delete_all_data():
                    print("All data deleted successfully.")
                else:
                    print("No data to be deleted. DB is empty.")
                    
        else:
            print("Invalid option selected. Please try again.")
    else:
        db.close_connection()
        exit("Program closed")