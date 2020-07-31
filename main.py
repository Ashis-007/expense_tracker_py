from datetime import date
from sys import exit
import sqlite3 as sql

class Database:

    def __init__(self):
        self.__conn = sql.connect("expense.db")
        self.__cur = self.__conn.cursor()
        self.create_table()


    def create_table(self):
        try:
            self.__cur.execute("""
            CREATE TABLE IF NOT EXISTS 
            expenses(ID INTEGER PRIMARY AUTOINCREMENT, 
            AMOUNT INTEGER NOT NULL, 
            NOTE TEXT,
            DATE INTEGER NOT NULL)
            """)
            print("Table created successfully!")
            return True
        except:
            print("Could not create table for DB")
            return False


    def insert_data(self, data):
        try:
            self.__cur.execute("INSERT INTO expenses(AMOUNT, NOTE, DATE) VALUES(?, ?, ?)", data)
            return True
        except:
            print("Could not insert data into DB")
            return False


    def fetch_all_data(self):
        try:
            with self.__conn:
                self.__cur.execute("SELECT AMOUNT, NOTE, DATE FROM expenses")
                return self.__cur.fetchall()
        except:
            print("Could not fetch data from DB!")
            return False


# amount
# note/description
# date

def input_expense():
    amount = int(input("Enter amount: "))
    note = input("Enter note/desciption: ")
    current_date = date.today().strftime("%d/%m/%y")


def show_menu():
    print("""
    == MENU ==
    press 1 to add a new expense
    press 2 to see all expenses
    press 3 to see all expenses by given date
    press 4 to export your expenses into an excel file
    """)


def save_to_db(amount, note, current_date):
    pass


if __name__ == "__main__":
    print("=== Welcome to your own personalised Expense_Tracker! ===")
    choice = 4
    while choice is not 4:
        pass
    else:
        show_menu()
        exit("Program closed")