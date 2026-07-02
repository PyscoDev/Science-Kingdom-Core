import json

def entry():
    current_date = input("Enter the date(DD/MM/YYYY):")
    entry_of_today = input("How was your day?:\n")

    try:
        with open("journal_data.json", 'r') as file:
            journal_data = json.load(file)
    except FileNotFoundError:
        journal_data = {}
    
    journal_data[current_date] = entry_of_today

    with open("journal_data.json", 'w') as file:
        json.dump(journal_data, file, indent=4)
        print("Saved!")

def deletion():
    try:
        with open("journal_data.json",'r') as file:
            journal_data=json.load(file)
            if not journal_data:
                print("No data to show!")
                return
            
            user_input=input("Enter the date stamp you want to delete(DD/MM/YYYY):")
            if user_input not in journal_data:
                print("No entry for the date!")
                return
            
            del journal_data[user_input]

            with open("journal_data.json",'w') as file:
                json.dump(journal_data,file,indent=4)
                print("Saved!")
    
    except FileNotFoundError:
        print("No File!")
          
def entry_search():
    try:
        with open("journal_data.json",'r') as file:
            journal_data=json.load(file)
            if not journal_data:
                print("No data to show!")
                return

            user_input=input("Enter date to see its entry(DD/MM/YYYY):")
            if user_input not in journal_data:
                print("No entry for the date!")
                return
            
            the_entry=journal_data[user_input]
            print(the_entry)
    
    except FileNotFoundError:
        print("No file!")


while True:
    try:
        user_choice=int(input("What do you want to do?\n1.New Entry\n2. Delete\n3. Search entry\n4. Exit"))
    except ValueError:
        print("Enter integer")
        continue
    
    if user_choice==1:
        entry()
    elif user_choice==2:
        deletion()
    elif user_choice==3:
        entry_search()
    elif user_choice==4:
        print("Thank you for visiting!")
        break
    else:
        print("Invalid Entry!Retry!")