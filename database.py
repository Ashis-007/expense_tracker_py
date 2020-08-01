import sqlite3 as sql

class Database:

    def __init__(self):
        self.__conn = sql.connect("expense.db")
        self.__cur = self.__conn.cursor()
        self.create_table()


    def create_table(self):
        try:
            self.__cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY AUTOINCREMENT, 
            amount INTEGER NOT NULL, 
            note TEXT,
            date INTEGER NOT NULL)
            """)
            self.__conn.commit()
            return True
        except Exception as err:
            print("Could not create table for DB", err)
            return False


    def insert_data(self, data):
        try:
            self.__cur.execute("INSERT INTO expenses(amount, note, date) VALUES(?, ?, ?)", data)
            self.__conn.commit()
            return True
        except Exception as err:
            print("Could not insert data into DB", err)
            return False


    def fetch_all_data(self):
        try:
            self.__cur.execute("SELECT amount, note, date FROM expenses")
            self.__conn.commit()
            return self.__cur.fetchall()
        except Exception as err:
            print("Could not fetch data from DB!", err)
            return False


    def delete_all_data(self):
        try:
            self.__cur.execute("DROP TABLE expenses")
            self.__conn.commit()
            return True
        except Exception as err:
            print("Could not delete data from DB!", err)
            return False


    def close_connection(self):
        self.__cur.close()
        self.__conn.close()