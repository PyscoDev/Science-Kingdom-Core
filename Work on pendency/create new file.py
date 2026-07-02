import os
import pptx  # For PowerPoint
from openpyxl import Workbook  # For Excel
from docx import Document  # For Word
import json #For json
import csv #For csv
import datetime
import pandas as pd

def create_file(file_type, filename):
    """Creates a new file of the specified type."""
    try:
        if file_type == "ppt":
            prs = pptx.Presentation()
            prs.save(filename + ".pptx")
            print(f"PowerPoint file '{filename}.pptx' created.")
        elif file_type == "excel":
            wb = Workbook()
            wb.save(filename + ".xlsx")
            print(f"Excel file '{filename}.xlsx' created.")
        elif file_type == "word":
            doc = Document()
            doc.save(filename + ".docx")
            print(f"Word file '{filename}.docx' created.")
        elif file_type == "json":
            data = {}  # Start with an empty dictionary
            with open(filename + ".json", 'w') as f:
                json.dump(data, f, indent=4)
            print(f"JSON file '{filename}.json' created.")
        elif file_type == "csv":
            DATA_DIR = "financial_data"
            CATEGORIES = ["Need", "Personal", "Investment", "Development"]
            os.makedirs(DATA_DIR, exist_ok=True)
            for category in CATEGORIES:
                filename = os.path.join(DATA_DIR, f"{category}.csv")
                if not os.path.exists(filename):
                    df = pd.DataFrame(columns=["Date", "Amount", "Mode", "Type", "Description", "Category"])
                    df.to_csv(filename, index=False, encoding="utf-8")
            print("CSV files created (or already existed).")
        elif file_type == "text":
            with open(filename + ".txt", "w") as f:
                f.write("")  # Create an empty text file
            print(f"Text file '{filename}.txt' created.")
        else:
            print("Invalid file type.")
            return

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    while True:
        print("\nFile Creation Tool")
        print("1. Create PowerPoint (.pptx)")
        print("2. Create Excel (.xlsx)")
        print("3. Create Word (.docx)")
        print("4. Create JSON (.json)")
        print("5. Create CSV files")
        print("6. Create Text (.txt)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice in ("1", "2", "3", "4", "5", "6"):
            filename = input("Enter the filename (without extension): ")

            if choice == "1":
                create_file("ppt", filename)
            elif choice == "2":
                create_file("excel", filename)
            elif choice == "3":
                create_file("word", filename)
            elif choice == "4":
                create_file("json", filename)
            elif choice == "5":
                create_file("csv", filename)
            elif choice == "6":
                create_file("text", filename)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")
