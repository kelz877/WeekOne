#Write an app which asks users for input and then prints the factorial of that number

#ask the user for a number
number = int(input("Please enter a number: "))


def factorial(number):
  result=1
  while number >= 1:
    result = result * number
    number = number - 1
  return result

factorial_user_input = factorial(number)

print(f"The factorial of {number} is {factorial_user_input}.")