import time

def Task_View():
    Task_List=[]
    Task_File=open('Tasks.txt','r')
    for line in Task_File:
        Task_List.append(line)
    Task_File.close()
    print("Task List:\n")
    for index,task in enumerate(Task_List,start=1):
        print(index,":",task)

def Add_Task():
    Task_File=open('Tasks.txt','a+')
    new_task=input("Enter the task")
    Task_File.seek(0)
    first_char=Task_File.read(1)
    if not first_char:
        Task_File.write(new_task)
    else:
        Task_File.write('\n'+new_task)
    Task_File.close()

def Task_Done():
    Task_List=[]
    Task_File=open('Tasks.txt','r')
    Task_File.seek(0)
    first_char=Task_File.read(1)
    if not first_char:
        print("\n No Task to Delete.")
    else:
        for line in Task_File:
            Task_List.append(line)
        Task_File.close()
        task_num=int(input("Enter the task number that is completed"))
        if task_num<1 or task_num>len(Task_List):
            print("Are you dumb?")
        else:
            Task_List.pop(task_num-1)
            with open('Tasks.txt','w') as file:
                for task in Task_List:
                    file.write(task.strip()+'\n')
            file.close

def user_choice(): 
    while True:
        user=int(input("\nChoose what you want to do\n1.View Task on List\n2.Add Task to List\n3.Mark Task as Complete\n4.Exit\n"))
        if user==4:
            print("See you soon!")
            time.sleep(2)
            break
        elif user==3:
            Task_Done()
        elif user==2:
            Add_Task()
        elif user==1:
            Task_View()
        else:
            print("Invalid Input!Try Again!")

user_choice()
