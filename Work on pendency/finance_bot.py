import csv
import datetime
import os
import pandas as pd

FINANCIAL_RECORDS = "my_transaction.csv"
TRANSACTION_TYPES = {"C": "Credit", "D": "Debit"}

def get_finance_data():
    """Reads financial data from a CSV file."""
    transactions = []
    try:
        if not os.path.exists(FINANCIAL_RECORDS):
            print(f"Error: File '{FINANCIAL_RECORDS}' not found.")
            return []

        with open(FINANCIAL_RECORDS, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not row.get("Date") or not row.get("Amount"):
                    print(f"Warning: Skipping incomplete row: {row}")
                    continue

                try:
                    row["Date"] = datetime.datetime.strptime(row["Date"], "%Y-%m-%d").date()
                    row["Amount"] = float(row["Amount"])
                    transactions.append(row)
                except ValueError as ve:
                    print(f"ValueError in row: {row}. Error: {ve}")
                    continue
    except Exception as e:
        print(f"An unknown error occurred: {e}")
        return []
    return transactions

def get_month_year_input():
    """Gets valid year and month input from the user."""
    while True:
        try:
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            if not 1 <= month <= 12:
                raise ValueError
            return year, month
        except ValueError:
            print("Invalid input. Please enter a valid year and month.")

def get_monthly_summary(year, month):
    """Calculates monthly financial summary."""
    transactions = get_finance_data()
    if not transactions:
        return None

    summary = {
        "Personal": {"Income": 0, "Expense": 0},
        "Bussiness": {"Income": 0, "Expense": 0},
        "Account Balances": {}
    }

    for transaction in transactions:
        if transaction["Date"].year == year and transaction["Date"].month == month:
            amount = transaction["Amount"]
            transaction_type = transaction["Type"]
            category = transaction["Category"]
            description = transaction["Description"].lower()

            if category == "Transfer":
                continue

            # Treat "Null" category with "deposit" in description as "Business" Expense
            if category == "Null" and "deposit" in description:
                category = "Bussiness"
                transaction_type = "D"

            # Treat "Deposit" category as "Business" Expense
            if category == "Deposit":
                category = "Bussiness"
                transaction_type = "D"

            if category not in summary:
                summary[category] = {"Income": 0, "Expense": 0}

            if transaction_type == "C":
                summary[category]["Income"] += amount
            elif transaction_type == "D":
                summary[category]["Expense"] += amount

            summary["Account Balances"].setdefault(category, 0)
            if transaction_type == "C":
                summary["Account Balances"][category] += amount
            elif transaction_type == "D":
                summary["Account Balances"][category] -= amount

    return summary

def display_monthly_summary():
    """Displays the monthly financial summary."""
    year, month = get_month_year_input()
    if not year or not month:
        return

    summary = get_monthly_summary(year, month)
    if not summary:
        print("No transactions found for this month.")
        return

    print(f"\n{datetime.date(year, month, 1).strftime('%B %Y')} Summary:")
    for category in summary.keys():
        if category == "Account Balances":
            continue
        print(f"{category}:")
        income = summary[category].get("Income", 0)
        expense = summary[category].get("Expense", 0)
        print(f"  Total Income: ₹{income:.2f}")
        print(f"  Total Expense: ₹{expense:.2f}")
        print(f"  Net Cash Flow: ₹{income - expense:.2f}")
    print("Account Balances:")
    for account, balance in summary["Account Balances"].items():
        print(f"  {account}: ₹{balance:.2f}")

def display_finance_data_formatted():
    """Displays financial data in a formatted table."""
    data = get_finance_data()
    if data:
        print("Data loaded successfully:")
        print("-" * 100)
        print("{:<12} {:<10} {:<10} {:<15} {:<30} {:<20}".format("Date", "Amount", "Mode", "Type", "Description", "Category"))
        print("-" * 100)
        for transaction in data:
            print("{:<12} {:<10.2f} {:<10} {:<15} {:<30} {:<20}".format(
                transaction['Date'].strftime("%Y-%m-%d"),
                transaction['Amount'], transaction['Mode'],
                TRANSACTION_TYPES.get(transaction['Type'], "Unknown"),
                transaction['Description'], transaction['Category']
            ))
        print("-" * 100)
    else:
        print("No financial data to display.")

def display_finance_data_pandas():
    """Displays financial data using pandas."""
    try:
        df = pd.read_csv(FINANCIAL_RECORDS, parse_dates=["Date"])
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.colheader_justify', 'left')
        if not df.empty:
            print("Data loaded successfully (using pandas):")
            print(df)
        else:
            print("No financial data to display.")
    except FileNotFoundError:
        print(f"File not found: {FINANCIAL_RECORDS}")
    except Exception as e:
        print(f"An error occurred while reading with pandas: {e}")

while True:
    print("\nFinancial Tracking Bot")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Monthly Summary")
    print("4. Display Data (Formatted)")
    print("5. Display Data (Pandas)")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pass  # Implement add_income
    elif choice == "2":
        pass  # Implement add_expense
    elif choice == "3":
        display_monthly_summary()
    elif choice == "4":
        display_finance_data_formatted()
    elif choice == "5":
        display_finance_data_pandas()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
