from contextlib import contextmanager
import mysql.connector
from logging_setup import setup_logger

logger = setup_logger("db_helper")

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ManavSri14@",
        database="expense_manager",
    )

    if connection.is_connected():
        print("Connection Successful")

    else:
        print("Connection Failed")


    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses;")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)



def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s;", (expense_date,))
        expenses = cursor.fetchall()
        # for expense in expenses:
        #     print(expense)
        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
        (expense_date, amount, category, notes)
        )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date=%s",(expense_date,)
        )

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            f'''
            SELECT category, SUM(amount) as total
            FROM expense_manager.expenses
            Where expense_date BETWEEN %s and %s
            GROUP BY category; 
            ''', (start_date, end_date)
        )
        data = cursor.fetchall()
        for category in data:
            print(category)
        return data




if __name__ == "__main__":
    # fetch_all_records()
    # fetch_expenses_for_date("2026-09-27")
    # insert_expense("2026-09-27", "1100", "Visit", "Westside and dinner")
    # fetch_all_records()

    print("******Expenses on 2026/09/27*******")
    fetch_expenses_for_date("2026-09-27")
    # #
    # print("******Delete Expense on 2026/09/27*******")
    # delete_expense("2026-09-27")
    # #
    # print("******Expense on 2026/09/27 after deleting the expense*******")
    # fetch_expenses_for_date("2026-09-27")
    data = fetch_expense_summary('2024-08-01','2024-08-05')
    print("Data: ", data)

def fetch_all_expenses_and_group_by_months():
    logger.info(f"fetch_all_expenses_and_group_by_months called ")
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT
    YEAR(expense_date) AS year,
    MONTH(expense_date) AS month_number,
    MONTHNAME(expense_date) AS month_name,
    ROUND(AVG(amount), 2) AS average_transaction,
    COUNT(*) AS total_transactions
FROM expense_manager.expenses
GROUP BY
    YEAR(expense_date),
    MONTH(expense_date),
    MONTHNAME(expense_date)
ORDER BY
    year,
    month_number;""")
        expenses = cursor.fetchall()
        # for expense in expenses:
        #     print(expense)
        return expenses