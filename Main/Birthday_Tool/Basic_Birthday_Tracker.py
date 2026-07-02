import uuid
import json

def add_birthday():
    new_id=str(uuid.uuid4())
    print("Enter all details in number.")
    
    while True:
        try:
            the_name=input("Enter the name:")
            the_date=int(input("Enter the date:"))
            the_month=int(input("Enter the month:"))
            the_year=int(input("Enter the Year:"))
            break
        except ValueError:
            print("Enter date,month,year in numeric format.")

    new_entry={"name":the_name,"date":the_date,"month":the_month,"year":the_year}

    try:
        with open("birthdays.json",'r') as file:
            birthday_list=json.load(file)
            birthday_list[new_id]=new_entry
        with open("birthdays.json",'w') as file:
            json.dump(birthday_list,file,indent=4)
    except FileNotFoundError:
        with open("birthdays.json",'w') as file:
            birthday_list={new_id:new_entry}
            json.dump(birthday_list,file,indent=4)
    
def view_birthday():
    try:
        with open("birthdays.json",'r') as file:
            birthday_data=json.load(file)
    except FileNotFoundError:
        print("No file found.")
        return

    if not birthday_data:
        print("No data in file")
        return
    else:
        index=1
        for i in birthday_data:
            individual_data=birthday_data[i]
            print(f"{index}.{individual_data['name']}-{individual_data['date']}/{individual_data['month']}/{individual_data['year']}")
            index+=1
    
def chk_month():
    try:
        with open("birthdays.json",'r') as file:
            birthday_data=json.load(file)
            if not birthday_data:
                print("No data to show.")
                return
    except FileNotFoundError:
        print("No file found.")
        return
    
    while True:
        try:
            user_input=int(input("What do you want to do?\n1.Check for current month.\n2.Check for a specific month."))
            if user_input==1:
                the_month=datetime.date.today().month
                break
            elif user_input==2:
                while True:
                    try:
                        the_month=int(input("Enter the month in integer"))
                        break
                    except ValueError:
                        print("Wrong entry. Try again!")
                break
            else:
                print("Invalid Choice!Try again.")
        except ValueError:
            print("Invalid Entry!Try again.")

    result=[]
    for i in birthday_data:
        if birthday_data[i]['month']==the_month:
            result.append(birthday_data[i]['name'])
    if not result:
        print("No person found for the given month.")
        return
    else:
        print("Here is the list of person(s) who have birthday on the given month:")
        for i in result:
            print(i)

def chk_name():
    try:
        with open("birthdays.json",'r') as file:
            birthday_data=json.load(file)
            if not birthday_data:
                print("File is empty.")
                return
    except FileNotFoundError:
        print("No file found.")
        return
    
    user_input=input("Enter the name you want to search for:")
    result=[]
    
    for i in birthday_data:
        if birthday_data[i]['name'].strip().lower()==user_input.strip().lower():
            result.append(birthday_data[i])
    if not result:
        print("NO match found.")
        return
    
    print("Here is the list of matches found:")
    for i in result:
        print(i)

def deletion():

    #will add security key later once security module is created

        try:
            with open("birthdays.json",'r') as file:
                birthday_data=json.load(file)
                if not birthday_data:
                    print("File is already empty.")
                    return

                id_list=[]
                print("Uid.Details")
                for i in birthday_data:
                    id_list.append(i)
                    print(f"{i}.{birthday_data[i]}")
        except FileNotFoundError:
            print("No data to delete.\n")
            return
        
        while True:
            id_to_delete=input("Enter the Uid to delete:")
            if id_to_delete not in id_list:
                print("\nNo such Uid found.\n Check the Uid and try again.")
            else:
                while True:
                    user_choice=input("Are you sure?[Y/N]:")
                    if user_choice.strip().upper()=='Y':
                        del birthday_data[id_to_delete]
                        print("Successfully deleted.\nUpdated data:")
                        
                        if not birthday_data:
                            print("File is empty now.")
                        for i in birthday_data:
                            print(f"{i}.{birthday_data[i]}\n")
                        with open("birthdays.json",'w') as file:
                            json.dump(birthday_data,file,indent=4)
                        break
                    elif user_choice.strip().upper()=='N':
                        print("Deletion terminated.")
                        return
                    else:
                        print("Invalid choice.Retry!")
            break


while True:
    try:
        user_input=int(input("1.Add birthday\n2.Read whole list\n3.Check for this month\n4.Search by name\n5.Delete a entry\n6.Exit\n"))
        if user_input==6:
            print("Thank you for using me.")
            break
        elif user_input==5:
            deletion()
        elif user_input==4:
            chk_name()
        elif user_input==3:
            chk_month()
        elif user_input==2:
            view_birthday()
        elif user_input==1:
            add_birthday()
        else:
            print("Invalid Choice!! Retry!!")
    except ValueError:
        print("Invalid Choice!! Retry!!")
