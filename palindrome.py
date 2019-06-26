#create an app that detects if the input word is a palindrome or not

#ask for the user input
user_choice = input("Please provide a word for the palindrome check: ")



#reverse the word
def reverse_word(word):
  reversed = ""
  for index in range(len(word) - 1, -1, -1):
    reversed += word[index]
  return reversed

#test the reverse word function
print(reverse_word(user_choice))

reverse_user = (reverse_word(user_choice))

#check if the original word and reversed word are ==
def palindrome(word, reverse_word):
  if word == reverse_word:
    return True
  else:
    return False

print(palindrome(user_choice, reverse_user))