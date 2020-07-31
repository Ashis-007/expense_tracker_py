from datetime import date
from sys import exit
from database import Database

def input_expense():
    amount = int(input("Enter amount: "))
    note = input("Enter note/desciption: ")
    current_date = date.today().strftime("%d/%m/%y")
    return [amount, note, current_date]


def show_menu():
    print("""
    == MENU ==
    press 1 to add a new expense
    press 2 to see all expenses
    press 3 to see all expenses by given date
    press 4 to export your expenses into an excel file
    press 5 to exit
    """)


if __name__ == "__main__":
    db = Database() # instance of class Database

    print("=== Welcome to your own personalised Expense_Tracker! ===")
    choice = 0
    while choice is not 5:
        show_menu()
        choice = int(input("Choose your option: "))
        if choice == 5:
            continue
        elif choice == 1:
            data = input_expense()
            db.insert_data(data)
        elif choice == 2:
            data = db.fetch_all_data()
            print(data)
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("Invalid option selected. Please try again.")
    else:
        db.close_connection()
        exit("Program closed")