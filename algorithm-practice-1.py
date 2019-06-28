#remove the duplicates from the array
name_list = ["Bob", "Tina", "Linda", "Louise", "Gene", "Bob", "Linda"]

#loop through the array and if you see a new name, print to the new array
#if you see a name that has already been added, skip to the next name. 

def remove_duplicates(list):
    new_list = []
    for name in list:
        if name not in new_list:
            new_list.append(name)
    return new_list

new_list_of_names = remove_duplicates(name_list)
#print a new array

print(new_list_of_names)



#write a program which returns the largest number in an array
number_list = [1, 3, 4, 5, 6, 7, 8, 9, 100, 10, 2, 11]


#def function which takes an array as the argument
def largest_number(list):
    #create new variable which will be equal to the first value in the array
    largest = list[0]  
#since we are looking at parcitular values in the array and not the array as a whole, or the length we will need to create a new variable that looks at each value in array
    #begin the loop
    for number in list:
        #if the new variable (which is set to the first data point in the loop) is larger than the next number in the list, do not change largest
        if largest > number:
            continue
        else:
            #if largest is not greater than number, number will replace the value of largest and the loop will continue
            largest = number
    return largest

largest_in_list = largest_number(number_list)

print(largest_in_list)


#find the smallest number in an array

numbers = [100, 99, 98, 90, 80, 79, 30, 2, 40, 12, 33, 11, 999]

def smallest_number(numbers):
  smallest = numbers[0]
  for number in numbers:
    if smallest < number:
      continue
    else:
      smallest = number
  return smallest

smallest_num = smallest_number(numbers)

print(smallest_num)

#find the missing number in an array of numbers between 0 and 9. 
array_missing = [0, 1, 2, 3, 5, 6, 7, 8, 9]


#define the function to pass the array through it
def missing_number(array_missing):
    #define the range. since we know the last number in the array won't be missing, we can remove one off the back of the array
    for number in range(0, len(array_missing) - 1):
        #if number + 1 is not equal to the iterating index + 1, that means the number is missing from the index
        if number + 1 != array_missing[number + 1]:
            #assign a new variable as the number + 1
            missing = number + 1
            break
    return missing

missing = missing_number(array_missing)

print(missing)



#Assignment: given an array [1,2,3,4,5] write a function that duplicates the array ([1,2,3,4,5,1,2,3,4,5]), you may modify or create a new array.
original_array = [1,2,3,4,5]

#create function
def duplicate_array(array):
    #create the empty array where you will store your new array
    new_array = []
    #iterate through all the values in the array
    for index in range(len(array)):
        #for every number in the array, add it to the new array
        new_array.append(array[index])
    #repeat one more time 
    for index in range(len(array)):
        new_array.append(array[index])
    return new_array

duplicated_numbers = duplicate_array(original_array)

print(duplicated_numbers)





