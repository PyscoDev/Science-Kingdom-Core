from birthdaymanager import BirthdayManager

bot=BirthdayManager()

if __name__ == "__main__":
    while True:
        try:
            user_input=int(input("1.Add birthday\n2.Read whole list\n3.Check for this month\n4.Search by name\n5.Delete a entry\n6.Exit\n"))
            if user_input==6:
                print("Thank you for using me.")
                break
            elif user_input==5:
                if not bot.data:
                    print("No data found")
                else:
                    birthday_list=bot.view_birthday()
                    for i in birthday_list:
                        print(i)
                    ID=input("Enter the ID:")
                    print(bot.deletion(ID))
            elif user_input==4:
                if not bot.data:
                    print("No data found")
                else:
                    findname=input("Enter the full name:")
                    birthday_list=bot.chk_name(findname.lower())
                    presence=next(birthday_list,None)
                    if presence == None:
                        print("No data was found!")
                    else:
                        print(presence)
                        for i in birthday_list:
                            print(i)
            elif user_input==3:
                if not bot.data:
                    print("No data found")
                else:
                    try:
                        findmonth=int(input("Enter the month:"))
                        birthday_list=bot.chk_month(findmonth)
                        presence=next(birthday_list,None)
                        if presence == None:
                            print("No data was found!")
                        else:
                            print(presence)
                            for i in birthday_list:
                                print(i)
                    except ValueError:
                        print("Only interger value allowed in this field!")

            elif user_input==2:
                if not bot.data:
                    print("No data found")
                else:
                    birthday_list=bot.view_birthday()
                    for i in birthday_list:
                        print(i)
            elif user_input==1:
                print("Enter all date/month/year in number. Name in the format: First-Middle-Last")
                while True:
                    try:
                        the_name=input("Enter the name:")
                        the_date=int(input("Enter the date:"))
                        the_month=int(input("Enter the month:"))
                        the_year=int(input("Enter the Year:"))
                        break
                    except ValueError:
                        print("Enter date,month,year in numeric format.")
                bot.add_birthday(the_name,the_date,the_month,the_year)
            else:
                print("Invalid Choice!! Retry!!")
        except ValueError:
            print("Invalid Choice!! Retry!!")
