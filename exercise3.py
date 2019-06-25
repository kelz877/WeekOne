#Write an app which separatly takes first name and last name of the user. Once the name is taken print out the following message: 

#Hello, My name is FirstName, LastName 

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

def greeting(first, last):
  print(f"Hello, My name is {first}, {last}")

greeting(first_name, last_name)