#take input from the user and find out if that number is prime or not

#get input from user
user_input = int(input("Please enter a whole number: "))

#create function to identify number is prime
def prime_number(number):
  #create a range to loop through between 2 and num-1
  for i in range(2, number - 1):
    if number % i == 0:
      return "This is not a prime number"
    else:
      return "This is a prime number"

print(prime_number(user_input))
