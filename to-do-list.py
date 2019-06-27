#Create a To Do application
print("Hello and welcome to your To Do list!")

#create an empty array to store the data from inputs
to_do_list = []

#When the app starts it should present user with the following menu: 
    #Press 1 to add task 
    #Press 2 to delete task 
    #Press 3 to view all tasks 
    #Press q to quit 
#function to display menu
def display_menu():
  print("""
  Press 1 to add a task
  Press 2 to delete a task
  Press 3 to view all tasks
  Press q to quit
  """)


#function 1 to Add tasks
def add_task():
  task_name = input("what is the name of the task?  ")
  priority = input("Please enter task priority: Low, Medium, or High:  ")
  task = {
    "Task Name": task_name,
    "Priority": priority
    }
  to_do_list.append(task)
  #print(to_do_list)

#function 2 to delete tasks
def delete_task():
    #need to view the list
    view_list()
    #have the user select a number to delete the task 
    delete_item = int(input("input the number of the task you want to delete: "))
    del to_do_list[delete_item -1]




#function 3 to view all tasks
def view_list():
  for index in range(0, len(to_do_list)):
    print(f"{index + 1} - {to_do_list[index]['Task Name']} - {to_do_list[index]['Priority']}")

#assign user input as an empty string.
user_input = ""


while user_input != "q":
  #Print all of the options at once for the user  
  #if/else statements for what happens if the user chooses each of the inputs
    display_menu()
    user_input = input("What do you want to do? ")
  
    if user_input == "1":
        add_task()

    elif user_input == "2":
        delete_task()
    
    elif user_input == "3":
        view_list()
  





#The user should only be allowed to quit when they press 'q'. 





#Allow the user to view all the tasks in the following format: 
  #1 - Wash the car - high 
  #2 - Mow the lawn - low 

 

#* Store each task in a dictionary and use 'title' and 'priority' as keys of the dictionary. 

#* Store each dictionary inside an array. Array will represent list of tasks.  